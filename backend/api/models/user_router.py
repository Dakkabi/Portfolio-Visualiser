from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.database.crud.user_crud import create_db_user
from backend.database.models.user_model import User
from backend.database.session import get_db
from backend.schemas.models.user_schema import UserSchema, UserCreate
from backend.services.security.auth_service import get_current_active_user

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@user_router.get("/me", response_model=UserSchema)
def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@user_router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_db_user(db, user)
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="User with email already exists.",
        )