from sqlalchemy.orm import Session

from backend.database.models.user_model import User
from backend.schemas.models.user_schema import UserCreate
from backend.services.security.cryptography_service import get_password_hash


def get_db_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_db_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user