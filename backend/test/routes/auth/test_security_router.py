from fastapi.testclient import TestClient

from backend.test.conftest import *

client = TestClient(app)
url_prefix = "/api/encryption"

def test_derive_key_function():
    response = client.post(
        f"{url_prefix}/derive-key",
        json={"password": "test"}
    )
    assert response.status_code == 200
    secret_key_test1 = response.json()

    response = client.post(
        f"{url_prefix}/derive-key",
        json={"password": "test"}
    )
    secret_key_test2 = response.json()

    response = client.post(
        f"{url_prefix}/derive-key",
        json={"password": "family_guy"}
    )
    secret_key_family_guy3 = response.json()

    assert isinstance(secret_key_test1, str)
    assert secret_key_test1 != secret_key_family_guy3
    assert secret_key_test1 == secret_key_test2 # Deterministic
