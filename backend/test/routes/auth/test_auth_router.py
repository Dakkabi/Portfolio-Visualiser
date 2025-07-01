import pytest
from fastapi import status
from fastapi.testclient import TestClient

from backend.src.database.crud.user_crud import create_user
from backend.src.database.session import get_db
from backend.src.main import app
from backend.src.schemas.model.user_schema import UserCreate
from backend.src.services.auth.auth_service import decode_access_token
from backend.test.database.test_session import db

client = TestClient(app)

url_prefix = "api/auth"

@pytest.fixture(autouse=True)
def override_dependency_db(db):
    def _get_db_override():
        yield db
    app.dependency_overrides[get_db] = _get_db_override

def test_login_for_access_token(db):
    # Test Login Failure
    response = client.post(
        f"{url_prefix}/login",
        data={"username": "nobody@test.com", "password": "null"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Test Login Success
    new_user = UserCreate(
        email="success@test.com",
        password="something"
    )
    create_user(db, new_user)
    response = client.post(
        f"{url_prefix}/login",
        data={"username": new_user.email, "password": new_user.password},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == status.HTTP_200_OK

    payload = response.json()
    assert payload["token_type"] == "bearer"

    access_token = payload["access_token"]
    data = decode_access_token(access_token)
    assert data.get("sub") == new_user.email

