import pytest
from fastapi import HTTPException

from backend.src.services.security.auth_service import *


def test_authenticate_user_failure(db_user, get_test_db):
    # User found but incorrect password
    assert not authenticate_user(db_user.email, "None", get_test_db)

def get_access_token(email : str = None):
    if email is None:
        data = {}
    else:
        data = {"sub": email}
    access_token = create_access_token(data=data)
    return access_token

@pytest.mark.asyncio
async def test_get_current_user_success(db_user, get_test_db):
    access_token = get_access_token(db_user.email)

    returned_user = await get_current_user(access_token, get_test_db)
    assert returned_user.id == db_user.id

@pytest.mark.asyncio
async def test_get_current_user_failure(db_user, get_test_db):
    access_token = get_access_token(None)
    with pytest.raises(HTTPException):
        await get_current_user(access_token, get_test_db)

    access_token = "Invalid"
    with pytest.raises(HTTPException):
        await get_current_user(access_token, get_test_db)

    access_token = get_access_token("invalid-email")
    with pytest.raises(HTTPException):
        await get_current_user(access_token, get_test_db)

@pytest.mark.asyncio
async def test_get_current_active_user(db_user):
    returned_user = await get_current_active_user(db_user)
    assert returned_user.id == db_user.id