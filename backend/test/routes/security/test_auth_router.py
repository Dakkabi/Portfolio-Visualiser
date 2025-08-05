from fastapi.testclient import TestClient

from backend.src.main import app

client = TestClient(app)

def test_login_for_access_token_unauthorised():
    response = client.post(
        "/api/auth/login",
        data={
            "username": "None",
            "password": "None",
        }
    )
    assert response.status_code == 401

def test_login_for_access_token_success(db_user):
    response = client.post(
        "/api/auth/login",
        data={
            "username": db_user.email,
            "password": "test"
        }
    )
    assert response.status_code == 200