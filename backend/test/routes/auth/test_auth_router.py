from fastapi.testclient import TestClient

from backend.src.main import app
from backend.test.conftest import get_user_argument

client = TestClient(app)

def test_login_for_access_token(get_user):
    response = client.post(
        "/api/auth/login",
        data={
            "username": "unknown",
            "password": "unknown"
        }
    )
    assert response.status_code == 401

    response = client.post(
        "/api/auth/login",
        data={
            "username": get_user_argument.email,
            "password": get_user_argument.password
        }
    )
    assert response.status_code == 200