from sqlalchemy.orm.session import Session

from backend.src.database.models.user_model import User
from backend.src.schemas.model.user_schema import UserCreate
from backend.src.services.auth.security_service import hash_password


def get_db_users(db: Session):
    return db.query(User).all()

def get_db_user(db: Session, user_id: int) -> type[User] | None:
    return db.query(User).filter(User.id == user_id).first()

def get_db_user_by_email(db: Session, email: str) -> type[User] | None:
    return db.query(User).filter(User.email == email).first()

def create_db_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        email=str(user.email),
        password=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user