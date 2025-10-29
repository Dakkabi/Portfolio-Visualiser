from datetime import timedelta, datetime, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from starlette import status

from backend.src.core.config_loader import settings
from backend.src.database.crud.user_crud import get_db_user_by_email
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.security.token_schema import TokenData
from backend.src.services.security.cryptography import verify_password

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

TOKEN_EXPIRY = 15 # In Minutes

def authenticate_user(email: str, password: str, db: Session) -> bool | type[User]:
    """
    Authenticate a given user by comparing their challenge inputs against the database.

    :param email: The user's email address.
    :param password: The challenge password.
    :param db: The database session.
    :return: False if credentials are invalid, else return the User row.
    """
    user = get_db_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, str(user.password)):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create an access token, appending it to the given data, with a specified expiration timer.

    :param data: Data to be encapsulated in an encoded token.
    :param expires_delta: The difference in minutes from the current time and when to expire.
    :return: A string representation of the JWT encoded access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRY)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    """
    Get the User row from a given access token.

    :param token: The token to be decoded.
    :param db: The database session.
    :return: The User row, using the email encapsulated as identification.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithm=[ALGORITHM])
        email = payload.get("sub")

        if email is None:
            raise credentials_exception

        token_data = TokenData(email=email)

    except InvalidTokenError:
        raise credentials_exception

    user = get_db_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    Get the current user but with more checks.

    :param current_user: An injected dependency.
    :return: The user row.
    """
    return current_user
