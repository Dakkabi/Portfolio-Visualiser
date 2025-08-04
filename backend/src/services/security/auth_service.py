from datetime import timedelta, timezone, datetime
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from starlette import status

from backend.src.core.config import settings
from backend.src.database.crud.user_crud import get_db_user_by_email
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.security.token_schema import TokenData
from backend.src.services.security.cryptography_service import verify_password

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def authenticate_user(email: str, password: str, db: Session = Depends(get_db)) -> User | bool:
    """Check if the user exists and the credentials match against the database.

    :param email: The user's email.
    :param password: The user's password.
    :param db: The database session.
    :return: The user if they are valid, False otherwise.
    """
    user = get_db_user_by_email(db, email)

    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create a JWT encoded access token and add an expiry value.

    :param data: The data to encode.
    :param expires_delta: How long the access token is valid for.
    :return: The encoded data as a string.
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
    """Retrieve the user from a given access token.

    :param token: The JWT encoded access token.
    :param db: The database session.
    :return: The user record from the database.

    :raises HTTPException: If the token is invalid or user does not exist.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
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

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """Return the authenticated user.

    Currently same implementation as `get_current_user`
    but any strict checks will be listed here.
    """
    return current_user

