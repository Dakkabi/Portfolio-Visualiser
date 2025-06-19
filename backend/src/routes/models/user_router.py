from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.user_crud import *
from backend.src.database.session import get_db
from backend.src.schemas.model.user_schema import UserSchema

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.get("/", response_model=List[UserSchema])
def get_all_users(db: Session = Depends(get_db())):
    return get_users(db)

@user_router.get("/{user_id}", response_model=UserSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

@user_router.post("/", response_model=UserSchema)
def user_post(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


