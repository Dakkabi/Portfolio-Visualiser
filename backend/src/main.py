import uvicorn
from fastapi import FastAPI

from backend.src.routes.models.user_router import user_router
from backend.src.routes.security.authentication_router import auth_router

app = FastAPI()

ROUTER_PREFIX = "/api"
app.include_router(auth_router, prefix=ROUTER_PREFIX)
app.include_router(user_router, prefix=ROUTER_PREFIX)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)