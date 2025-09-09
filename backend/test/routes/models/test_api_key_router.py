from starlette.testclient import TestClient

from backend.src.main import app
from backend.src.routes.models import api_key_router
from backend.src.schemas.models.api_key_schema import ApiKeyCreate

client = TestClient(app)

def _mock_validate_broker_api_keys(brokers_name: str, api_key: str, private_key: str = None):
    return True

def test_api_key_post(monkeypatch):
    monkeypatch.setattr(api_key_router, "validate_broker_api_keys", _mock_validate_broker_api_keys)

    api_key_request = ApiKeyCreate(
        api_key="test",
        private_key="test",
        broker_name="Trading212",
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

    api_key_request_wrong_broker = ApiKeyCreate(
        api_key="test",
        private_key="test",
        broker_name="None",
    )
    response = client.post(
        "/api/keys",
        json=api_key_request_wrong_broker.model_dump()
    )
    assert response.status_code >= 400

def test_api_key_get():
    response = client.get("/api/keys")
    assert response.status_code == 200

def test_api_key_get_by_brokers_name():
    response = client.get("/api/keys/Trading212")
    assert response.status_code == 200

    db_api_key = response.json()
    assert db_api_key["broker_name"] == "Trading212"

    response = client.get("/api/keys/Kraken")
    assert response.status_code == 404

def test_api_key_put(monkeypatch):
    monkeypatch.setattr(api_key_router, "validate_broker_api_keys", _mock_validate_broker_api_keys)
    api_key_request = ApiKeyCreate(
        api_key="randomised",
        private_key="randomised",
        broker_name="Trading212",
    )

    response = client.put(
        "/api/keys",
        json=api_key_request.model_dump()
    )
    assert response.status_code == 200

def test_api_key_delete():
    response = client.delete("/api/keys/Trading212")
    assert response.status_code == 200
