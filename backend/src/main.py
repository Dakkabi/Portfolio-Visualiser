from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.src.database.crud.broker_crud import read_file_into_broker_table
from backend.src.database.session import get_db
from backend.src.routes.auth.auth_router import auth_router
from backend.src.routes.models.user_router import user_router

@asynccontextmanager
async def lifespan(app: FastAPI):

    db_session = next(get_db())

    read_file_into_broker_table(db_session)

    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prefixUrl = "/api"
app.include_router(auth_router, prefix=prefixUrl)
app.include_router(user_router, prefix=prefixUrl)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)