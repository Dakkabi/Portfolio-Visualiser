import os

import requests.exceptions
from fastapi.testclient import TestClient

from backend.src.routes.models.api_key_router import *
from backend.test.conftest import *

client = TestClient(app)
url_prefix = "/api/api-keys"

@pytest.fixture(autouse=True)
def add_db_api_key(db, global_secret_key, dummy_active_user):
    broker_name = "Trading212"
    db_api_key = create_db_api_key(
        db,
        ApiKeyCreate(
            api_key="valid",
            private_key="valid",
            broker_name=broker_name
        ),
        global_secret_key,
        dummy_active_user.id
    )
    return db_api_key

def test_add_api_key_success(monkeypatch, db, dummy_active_user, global_secret_key):
    """Must come before test_add_api_key_failure"""
    broker_name = "Kraken"
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

    # No broker exists exception
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

    # API Key is invalid exception
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

def test_get_my_api_keys(db, add_db_api_key):
    response = client.get(
        f"{url_prefix}/"
    )
    assert response.status_code == 200
    data = response.json()[0]
    assert data["broker_name"] == "Trading212"

def test_get_my_decoded_api_keys(db, add_db_api_key, global_secret_key):
    response = client.post(
        f"{url_prefix}/decrypt/",
        json={
            "secret_key": global_secret_key
        }
    )
    assert response.status_code == 200
    data = response.json()[0]
    assert data["api_key"] == "valid"

def test_update_api_key_success(monkeypatch, global_secret_key):
    broker_name = "Trading212"
    monkeypatch.setitem(registry, broker_name, lambda key: None)

    randomstr = str(os.urandom(16))

    response = client.put(
        f"{url_prefix}/",
        json={
            "new_api_key": {
                "broker_name": broker_name,
                "api_key": randomstr,
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert decrypt_data(data["api_key"], global_secret_key) == randomstr

def test_update_api_key_failure(monkeypatch, global_secret_key):
    broker_name = "Trading212"
    monkeypatch.setitem(registry, broker_name, lambda key: True)

    # Broker not found exception
    response = client.put(
        f"{url_prefix}/",
        json={
            "new_api_key": {
                "broker_name": "unknown broker",
                "api_key": "valid",
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    )
    assert response.status_code == 404

    # Key not exist exception
    response = client.put(
        f"{url_prefix}/",
        json={
            "new_api_key": {
                "broker_name": "Kraken",
                "api_key": "valid",
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    )
    assert response.status_code == 404

    # API key is invalid (broker rejected)
    response = client.put(
        f"{url_prefix}/",
        json={
            "new_api_key": {
                "broker_name": "Trading212",
                "api_key": "valid",
                "private_key": "valid"
            },
            "secret_key": {
                "secret_key": global_secret_key
            }
        }
    )
    assert response.status_code == 400

def test_delete_api_key():
    response = client.delete(
        f"{url_prefix}/unknownBroker"
    )
    assert response.status_code == 404

    response = client.delete(
        f"{url_prefix}/Kraken"
    )
    assert response.status_code == 404

    response = client.delete(
        f"{url_prefix}/Trading212"
    )
    assert response.status_code == 200

    retrieve_api_keys = client.get(
        f"{url_prefix}/"
    )
    assert retrieve_api_keys.json() == []


