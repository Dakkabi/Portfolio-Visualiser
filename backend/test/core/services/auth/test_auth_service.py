import pytest

from backend.src.core.services.auth.auth_service import *

def test_authenticate_user_failure(get_user, get_test_db):
    assert not authenticate_user(get_user.email, "wrong-password", get_test_db)

@pytest.mark.asyncio
async def test_get_current_user_failure(get_test_db):
    with pytest.raises(HTTPException):
        no_email_token = create_access_token({})
        await get_current_user(no_email_token, get_test_db)

    with pytest.raises(HTTPException):
        await get_current_user("", get_test_db)

    with pytest.raises(HTTPException):
        no_user_token = create_access_token({"sub": "unknown"})
        await get_current_user(no_user_token, get_test_db)

@pytest.mark.asyncio
async def test_get_current_user_success(get_user, get_test_db):
    token_data = {"sub": get_user.email}
    valid_token = create_access_token(token_data)
    response_user = await get_current_user(valid_token, get_test_db)
    assert response_user is not None
    assert response_user.email == get_user.email

@pytest.mark.asyncio
async def test_get_current_active_user(monkeypatch, get_user):
    async def mock_get_current_user():
        return get_user

    monkeypatch.setattr("backend.src.core.services.auth.auth_service.get_current_user", mock_get_current_user)

    response_user = await get_current_active_user()

    assert response_user is not None

