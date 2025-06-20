from datetime import timedelta, datetime, timezone

import pytest
from fastapi import HTTPException

from backend.src.database.crud.user_crud import create_user
from backend.src.schemas.model.user_schema import UserCreate, UserSchema
from backend.src.services.auth.auth_service import *
from backend.test.database.test_session import db

def test_authenticate_user(db):
    assert not authenticate_user("no@one.com", "null", db)

    new_user = UserCreate(
        email="real@user.com",
        password="password"
    )
    create_user(db, new_user)

    assert not authenticate_user(new_user.email, "wrong_password", db)

    db_user = authenticate_user(new_user.email, new_user.password, db)
    assert db_user.email == new_user.email

def test_creating_and_decoding_tokens():
    data = {"message": "Hello, World!"}
    minutes_expiration_delta = 10

    token_with_no_set_exp = create_access_token(data=data)
    token_with_predefined_exp = create_access_token(data=data, expires_delta=timedelta(minutes=minutes_expiration_delta))

    # Default expiration timedelta may change
    assert "exp" in decode_access_token(token_with_no_set_exp)
    assert int(decode_access_token(token_with_predefined_exp)["exp"]) == int(datetime.now(timezone.utc).timestamp() + minutes_expiration_delta * 60)

@pytest.mark.asyncio
async def test_get_current_user(db):
    data = {"message": "Hello, World!"}
    token = create_access_token(data=data)

    with pytest.raises(HTTPException):
        await get_current_user(token, db)

    # InvalidTokenError
    with pytest.raises(HTTPException):
        await get_current_user("ThisIsntRight", db)

    data = {"sub": "not@real.com"}
    token = create_access_token(data=data)
    with pytest.raises(HTTPException):
        await get_current_user(token, db)

    new_user = UserCreate(
        email="not@real.com",
        password="test"
    )
    db_user = create_user(db, new_user)
    returned_user = await get_current_user(token, db)
    assert db_user.email ==  returned_user.email

    mock_user = UserSchema(id=2, email="user@example.com")
    result = await get_current_active_user(current_user=mock_user)
    assert result == mock_user
