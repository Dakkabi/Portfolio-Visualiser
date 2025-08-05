from fastapi.testclient import TestClient

from backend.src.database.models.user_model import User
from backend.src.main import app
from backend.src.services.security.auth_service import get_current_active_user

client = TestClient(app)

def test_get_user_me_unauthorised():
    response = client.get("/api/users/me")
    assert response.status_code == 401 # Unauthorised

def test_get_user_me_success(monkeypatch):
    def mock_get_current_active_user():
        return User(
            id=1,
            email="test@test.com",
            password="test"
        )

    app.dependency_overrides[get_current_active_user] = mock_get_current_active_user

    response = client.get("/api/users/me")
    assert response.status_code == 200