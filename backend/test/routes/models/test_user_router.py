import pytest
from fastapi.testclient import TestClient

from backend.src.core.services.auth.auth_service import get_current_active_user
from backend.src.main import app

client = TestClient(app)

@pytest.fixture
def get_unauthorized_client():
    """Temporarily rollback the dependency override on `get_current_active_user` to act out an unauthorized user."""
    original_override = app.dependency_overrides.get("get_current_active_user")

    app.dependency_overrides[get_current_active_user] = get_current_active_user

    yield

    app.dependency_overrides[get_current_active_user] = original_override


def test_user_get_me_success():
    response = client.get("/api/users/me")
    assert response.status_code == 200

def test_user_get_me_fail(get_unauthorized_client):
    response = client.get("/api/users/me")
    assert response.status_code == 401

def test_user_post():
    response = client.post(
        "/api/users",
        json={
            "email": "user@post.com",
            "password": "password",
        }
    )
    assert response.status_code == 200

    response = client.post(
        "/api/users",
        json={
            "email": "user@post.com",
            "password": "password",
        }
    )
    assert response.status_code == 400

