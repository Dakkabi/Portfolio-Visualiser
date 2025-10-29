from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.user_crud import create_db_user
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.user_schema import UserSchema, UserCreate
from backend.src.services.security.authentication import get_current_active_user

user_router = APIRouter(
    prefix="/users",
    tags=["User"],
)

@user_router.get("/me", response_model=UserSchema)
def get_me_endpoint(current_user: User = Depends(get_current_active_user)):
    return current_user

@user_router.post("/", response_model=UserSchema)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_db_user(db, user)
