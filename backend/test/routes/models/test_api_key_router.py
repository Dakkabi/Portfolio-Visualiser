from starlette.testclient import TestClient

from backend.src.main import app
from backend.src.routes.models import api_key_router
from backend.src.routes.models.api_key_router import validate_broker_api_keys
from backend.src.schemas.models.api_key_schema import ApiKeyRequest

client = TestClient(app)

def _mock_check_api_key_values_are_valid(brokers_name: str, api_key: str, private_key: str = None):
    return True

def test_api_key_post(monkeypatch):
    monkeypatch.setattr(api_key_router, "check_api_key_values_are_valid", _mock_check_api_key_values_are_valid)

    api_key_request = ApiKeyRequest(
        api_key="test",
        private_key="test",
        brokers_name="Trading212",
    )

    response = client.post(
        "/api/keys",
        json=api_key_request.model_dump()
    )
    assert response.status_code == 200

    # API Key already exists
    response = client.post(
        "/api/keys",
        json=api_key_request.model_dump()
    )
    assert response.status_code == 409

    api_key_request_wrong_broker = ApiKeyRequest(
        api_key="test",
        private_key="test",
        brokers_name="None",
    )
    response = client.post(
        "/api/keys",
        json=api_key_request_wrong_broker.model_dump()
    )
    assert response.status_code >= 400

def test_api_key_get_by_brokers_name():
    response = client.get("/api/keys/Trading212")
    assert response.status_code == 200

    db_api_key = response.json()
    assert db_api_key["brokers_name"] == "Trading212"

def test_api_key_put(monkeypatch):
    monkeypatch.setattr(api_key_router, "check_api_key_values_are_valid", _mock_check_api_key_values_are_valid)
    api_key_request = ApiKeyRequest(
        api_key="randomised",
        private_key="randomised",
        brokers_name="Trading212",
    )

    response = client.put(
        "/api/keys",
        json=api_key_request.model_dump()
    )
    assert response.status_code == 200

def test_api_key_delete():
    response = client.delete("/api/keys/Trading212")
    assert response.status_code == 200