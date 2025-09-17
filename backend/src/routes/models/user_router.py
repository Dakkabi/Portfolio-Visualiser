from alembic.util import status
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.src.core.services.auth.auth_service import get_current_active_user
from backend.src.database.crud.user_crud import create_db_user, get_db_user_by_email
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.user_schema import UserSchema, UserCreate

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/me", response_model=UserSchema)
def user_get_me(current_user: User = Depends(get_current_active_user)):
    """Get the current authenticated user from the access token."""
    return current_user

@user_router.post("/", response_model=UserSchema)
def user_post(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    if get_db_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_db_user(db, user)

@user_router.put("/email", response_model=UserSchema)
def user_put_email():
    pass

@user_router.put("/password", response_model=UserSchema)
def user_put_password():
    pass