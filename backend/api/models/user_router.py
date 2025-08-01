from fastapi import APIRouter, Depends

from backend.database.models.user_model import User
from backend.schemas.models.user_schema import UserSchema
from backend.services.security.auth_service import get_current_active_user

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@user_router.get("/me", response_model=UserSchema)
def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user