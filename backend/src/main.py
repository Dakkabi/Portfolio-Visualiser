import uvicorn
from fastapi import FastAPI

from backend.src.database.crud.broker_model import add_broker_from_file
from backend.src.database.session import get_db
from backend.src.routes.auth.auth_router import auth_router
from backend.src.routes.models.api_key_router import api_key_router
from backend.src.routes.models.user_router import user_router

app = FastAPI()

app.include_router(auth_router, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(api_key_router, prefix="/api")

if __name__ == "__main__":
    add_broker_from_file(next(get_db()))

    uvicorn.run(app, host="0.0.0.0", port=8000)