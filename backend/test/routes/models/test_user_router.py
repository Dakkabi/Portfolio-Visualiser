import pytest
from fastapi.testclient import TestClient

from backend.src.main import app
from backend.src.services.security.auth_service import get_current_active_user

client = TestClient(app)

@pytest.fixture
def unauthorised_client():
    """Remove the get_current_active_user override, to simulate a user that isn't logged-in."""

    # Store original dependency override
    original_get_current_active_user = app.dependency_overrides.get(get_current_active_user)
    app.dependency_overrides[get_current_active_user] = get_current_active_user

    yield

    # Restore original dependency override
    app.dependency_overrides[get_current_active_user] = original_get_current_active_user

def test_get_user_me_unauthorised(unauthorised_client):
    response = client.get("/api/users/me")
    assert response.status_code == 401 # Unauthorised

def test_get_user_me_success():
    response = client.get("/api/users/me")
    assert response.status_code == 200

def test_create_user():
    new_user = {
        "email": "create@user.com",
        "password": "to_be_hashed"
    }
    response = client.post(
        "/api/users",
        json=new_user
    )

    assert response.status_code == 200

    db_user = response.json()
    assert db_user["email"] == new_user["email"]