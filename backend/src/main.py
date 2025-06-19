from fastapi import FastAPI
import uvicorn
from backend.src.routes.auth.auth_router import auth_router
from backend.src.routes.models.user_router import user_router

app = FastAPI()

app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(user_router, prefix="/api", tags=["users"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)