from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from backend.database.session import get_db
from backend.schemas.security.token import Token
from backend.services.security.auth_service import authenticate_user, create_access_token

auth_router = APIRouter(
    prefix="/auth",
    tags=["Security"],
)

@auth_router.post("/login")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expiry = timedelta(minutes=1440)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expiry
    )

    return Token(access_token=access_token, token_type="bearer")