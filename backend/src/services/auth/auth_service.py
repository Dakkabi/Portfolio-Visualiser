from datetime import timedelta, timezone, datetime
from typing import Annotated

import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session

from backend.src.core.config import settings
from backend.src.database.crud.user_crud import get_user_by_email
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.auth.token_schema import TokenData
from backend.src.services.auth.security_service import verify_password

ALGORITHM = "HS256"
JWT_SECRET_KEY = settings.JWT_SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def authenticate_user(email: str, password: str, db: Session = Depends(get_db)) -> bool | type[User]:
    """
    Authenticate a user by email and password.

    :param email: The email of the user.
    :param password: The password inputted.
    :param db: The database connection.
    :return: User Schema if the user is authenticated, False otherwise.
    """

    user = get_user_by_email(db, email)
    if not user:
        return False

    if not verify_password(password, str(user.password)):
        return False

    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Return a dict signed with a JWT token.

    :param data: The data to encode.
    :param expires_delta: The token expiration time in seconds.
    :return: A dict signed with the JWT token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """
    Decode a JWT token.

    There should be zero reason to use this function over get_current_method(...)
    apart from debugging purposes.

    :param token: The JWT token.
    :return: The dict retrieved by decoding the JWT token.
    """
    return jwt.decode(token, JWT_SECRET_KEY, algorithms=ALGORITHM)


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
    ) -> type[User]:
    """
    Get the user from the email from the token.

    :param token: The signed token.
    :param db: The database connection.
    :return: User Schema if the user is authenticated, False otherwise.
    :raises: HTTPException if no email exists, invalid token or no user exists.
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

    user = get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception

    return user