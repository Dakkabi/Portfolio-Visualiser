from sqlalchemy.orm import Session

from backend.src.database.models.user_model import User
from backend.src.schemas.model.user_schema import UserCreate
from backend.src.services.security.cryptography_service import get_password_hash

def create_db_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user