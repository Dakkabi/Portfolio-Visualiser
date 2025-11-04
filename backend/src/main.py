from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from backend.src.database.crud.broker_crud import create_db_broker_from_file
from backend.src.database.session import get_db
from backend.src.routes.models.api_key_router import api_key_router
from backend.src.routes.models.user_router import user_router
from backend.src.routes.security.authentication_router import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs before FastAPI startup

    # Need to manually create the db at this stage
    db = next(get_db())
    create_db_broker_from_file(db)

    yield
    # Runs after FastAPI shutdown

app = FastAPI(lifespan=lifespan)

ROUTER_PREFIX = "/api"
app.include_router(auth_router, prefix=ROUTER_PREFIX)
app.include_router(user_router, prefix=ROUTER_PREFIX)
app.include_router(api_key_router, prefix=ROUTER_PREFIX)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)