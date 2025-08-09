import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.src.routes.models.user_router import user_router
from backend.src.routes.security.auth_router import auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

prefix = "/api"
app.include_router(auth_router, prefix=prefix)
app.include_router(user_router, prefix=prefix)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)