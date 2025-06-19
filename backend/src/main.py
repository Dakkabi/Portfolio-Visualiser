from fastapi import FastAPI
import uvicorn
from backend.src.routes.auth.auth_router import auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)