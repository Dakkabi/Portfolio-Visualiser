import pytest
from fastapi.testclient import TestClient

from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.main import app
from backend.src.services.auth.auth_service import get_current_active_user
from backend.test.database.test_session import db

client = TestClient(app)
url_prefix = "/api/users"

@pytest.fixture(autouse=True)
def override_dependency_db(db):
    def _get_db_override():
        yield db
    app.dependency_overrides[get_db] = _get_db_override

def test_create_and_get_users():
    response = client.post(
        f"{url_prefix}/",
        json={"email": "user@test.com", "password": "secret"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "user@test.com"

    # Get User By Id
    response = client.get(#
        f"{url_prefix}/999999"
    )
    assert response.status_code == 404

    response = client.get(
        f"{url_prefix}/1"
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "user@test.com"
    assert data["id"] == 1

    # Test Get All Users
    client.post(
        f"{url_prefix}/",
        json={"email": "new_user@test.com", "password": "secret"}
    )

    response = client.get(
        f"{url_prefix}/"
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == 1 and data[1]["id"] == 2
    assert data[0]["email"] == "user@test.com" and data[1]["email"] == "new_user@test.com"

"""
For the implementation for this test, see test_auth_router for test_login_for_access_token.

This hack is just for line coverage. The OAuth2 scheme has already been thoroughly tested.
"""
dummy_user = User(id=3, email="dummy@user.com", password="not_real")
app.dependency_overrides[get_current_active_user] = lambda: dummy_user

def test_get_me():
    response = client.get(f"{url_prefix}/me")
    assert response.status_code == 200
