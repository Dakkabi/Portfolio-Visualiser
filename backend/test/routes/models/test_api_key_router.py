import requests.exceptions
from fastapi.testclient import TestClient

from backend.src.routes.models.api_key_router import *
from backend.test.conftest import *

client = TestClient(app)
url_prefix = "/api/api-keys"

def test_add_api_key_success(monkeypatch, db, dummy_active_user, global_secret_key):
    """Must come before test_add_api_key_failure"""
    broker_name = "Trading212"
    monkeypatch.setitem(registry, broker_name, lambda key: None)

    client.post(
        f"{url_prefix}/",
        json={
            "api_key": {
                "broker_name": broker_name,
                "api_key": "valid",
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    )

    response = client.post(
        f"{url_prefix}/decrypt/{broker_name}",
        json={
            "secret_key": global_secret_key
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["api_key"] == "valid"

def test_add_api_key_failure(monkeypatch, db, global_secret_key, dummy_active_user):
    """Must come after test_add_api_key_success"""
    broker_name = "Trading212"
    broker_name2 = "Kraken"

    monkeypatch.setitem(registry, broker_name2, lambda key: True)

    json_with_no_broker_name = {
            "api_key": {
                "broker_name": "unknown broker",
                "api_key": "valid",
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    response = client.post(
        f"{url_prefix}/",
        json=json_with_no_broker_name
    )
    assert response.status_code == 404

    # Test creating a new key conflict
    create_db_api_key(
        db,
        ApiKeyCreate(
            api_key="valid",
            private_key="valid",
            broker_name=broker_name
        ),
        global_secret_key,
        dummy_active_user.id
    )
    response = client.post(
        f"{url_prefix}/",
        json={
            "api_key": {
                "broker_name": broker_name,
                "api_key": "valid",
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    )
    assert response.status_code == 409

    response = client.post(
        f"{url_prefix}/",
        json={
            "api_key": {
                "broker_name": broker_name2,
                "api_key": "valid",
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    )
    assert response.status_code == 400

