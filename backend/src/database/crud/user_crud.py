from sqlalchemy.orm import Session

from backend.src.database.models.user_model import User
from backend.src.schemas.models.user_schema import UserCreate
from backend.src.services.security.secrets import get_password_hash


def get_db_user_by_email(db: Session, email: str) -> type[User] | None:
    return db.query(User).filter(User.email == email).first()

def create_db_user(db: Session, new_user: UserCreate) -> User:
    db_user = User(
        email=new_user.email,
        password=get_password_hash(new_user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user