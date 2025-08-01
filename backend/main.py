import uvicorn
from fastapi import FastAPI

from backend.api.models.user_router import user_router
from backend.api.security.auth_router import auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/api")
app.include_router(user_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)