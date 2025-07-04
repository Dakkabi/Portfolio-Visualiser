import requests.exceptions
from fastapi import HTTPException
from fastapi.testclient import TestClient

from backend.src.database.crud.user_crud import create_db_user
from backend.src.routes.models.api_key_router import *
from backend.src.schemas.model.user_schema import UserCreate
from backend.test.conftest import *

client = TestClient(app)
url_prefix = "/api/api-keys"

@pytest.fixture
def setup_users(db : Session):
    db_user = create_db_user(
        db,
        UserCreate(
        email="api@key.com",
        password="router"
        )
    )
    return db_user

# Must come before api_key_failure
def test_add_api_key_success(monkeypatch, db, setup_users):
    broker_name = "Trading212"
    monkeypatch.setitem(registry, broker_name, lambda key: None)

def test_add_api_key_failure(monkeypatch, db, setup_users):
    broker_name = "Trading212"
    monkeypatch.setitem(registry, broker_name, lambda key: requests.exceptions.HTTPError)

