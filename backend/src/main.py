from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from backend.src.routes.models.user_router import user_router
from backend.src.routes.security.authentication_router import auth_router
from backend.src.services.models.broker_service import bulk_insert_brokers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs before FastAPI startup
    bulk_insert_brokers()

    yield
    # Runs after FastAPI shutdown

app = FastAPI(lifespan=lifespan)

ROUTER_PREFIX = "/api"
app.include_router(auth_router, prefix=ROUTER_PREFIX)
app.include_router(user_router, prefix=ROUTER_PREFIX)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)