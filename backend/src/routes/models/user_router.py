from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.src.database.crud.user_crud import create_db_user, get_db_user_by_email
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.model.user_schema import UserSchema, UserCreate
from backend.src.services.security.auth_service import get_current_active_user

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/me", response_model=UserSchema)
def get_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@user_router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if get_db_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_db_user(db, user)