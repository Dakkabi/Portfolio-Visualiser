from sqlalchemy.orm import Session

from backend.src.core.services.auth.cryptography_service import get_password_hash
from backend.src.database.models.user_model import User
from backend.src.schemas.models.user_schema import UserCreate


def get_db_user_by_email(db: Session, email: str) -> User | None:
    """Get user by email

    :param db: The database session
    :param email: The email to filter for the user.
    :return: User if it exists, else None.
    """
    return db.query(User).filter(User.email == email).first()

def create_db_user(db: Session, user: UserCreate) -> User:
    """Create a new user entry into the database.

    :param db: The database session.
    :param user: The user attributes to insert.
    :return: The created user.
    """
    db_user = User(
        email=user.email,
        password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user