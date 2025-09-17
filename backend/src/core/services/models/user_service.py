from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.src.core.services.auth.cryptography_service import verify_password
from backend.src.database.crud.user_crud import get_db_user, update_db_user
from backend.src.schemas.models.user_schema import UserUpdate


def update_user_password(
        db: Session,
        user_id: int,
        new_password: str,
        challenge_password: str
):
    db_user = get_db_user(db, user_id)
    if not verify_password(challenge_password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    return update_db_user(db, )
