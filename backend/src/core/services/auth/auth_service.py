from datetime import timedelta, datetime, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from starlette import status

from backend.src.core.config import settings
from backend.src.core.services.auth.cryptography_service import verify_password
from backend.src.database.crud.user_crud import get_db_user_by_email
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.auth.token import TokenData

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def authenticate_user(email: str, password: str, db: Session = Depends(get_db)) -> bool | User:
    """Authenticate the user by ensuring the user exists by email and ensure the password hash is correct.

    :param email: The user's email.
    :param password: The user's plaintext password.
    :param db: The database session.
    :return: False if invalid user, else return user.
    """
    user = get_db_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Generate a JWT encoded access token.

    :param data: The data to encode.
    :param expires_delta: The expiration time.
    :return: The JWT encoded string.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
    """Retrieve the user from an access token.

    :param token: The JWT encoded token.
    :param db: The database session.
    :return: The user model.

    :raises HTTPException: Invalid token or user data.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception

    user = get_db_user_by_email(db, token_data.email)
    if user is None:
        raise credentials_exception

    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Same implementation as get_current_user.

    :param current_user: get_current_user dependency injection.
    :return: The user model.
    """
    return current_user