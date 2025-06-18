from typing import Any
from sqlalchemy.orm.session import Session
from database.models.user import User
from schemas.user import UserCreate


def get_user(db: Session, user_id: int) -> type[User] | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> type[User] | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        email=str(user.email),
        # TODO: Hash The Password
        password=str(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user