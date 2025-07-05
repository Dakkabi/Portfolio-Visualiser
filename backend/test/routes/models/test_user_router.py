from fastapi.testclient import TestClient

from backend.test.conftest import *

client = TestClient(app)
url_prefix = "/api/users"

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
    assert data is not None

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
    assert len(data) > 0

def test_get_me():
    response = client.get(f"{url_prefix}/me")
    assert response.status_code == 200
