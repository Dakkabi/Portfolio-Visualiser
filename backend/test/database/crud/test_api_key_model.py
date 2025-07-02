import pytest
from cryptography.fernet import Fernet

from backend.src.database.crud.api_key_model import *
from backend.src.database.crud.broker_model import get_db_brokers
from backend.src.database.crud.user_crud import create_db_user
from backend.src.schemas.model.api_key_schema import ApiKeyCreate
from backend.src.schemas.model.user_schema import UserCreate
from backend.test.database.test_session import db

@pytest.fixture
def setup_users_db(db):

    db_user = create_db_user(db, UserCreate(email="apikey@test.com", password="hashed"))
    get_db_brokers(db) # Load brokers table

    return db_user

@pytest.fixture
def generate_secret_key():
    key = Fernet.generate_key()
    return key.decode("utf-8")


def test_crud_operations(db, setup_users_db, generate_secret_key):
    assert get_db_api_keys(db) == []

    db_api_key = create_db_api_key(
        db,
        ApiKeyCreate(
            broker_name="Trading212",
            api_key="Random",
            private_key="Random",
        ),
        generate_secret_key,
        setup_users_db.id
    )

    assert get_db_api_keys(db) == [db_api_key]
    assert get_db_api_keys_by_user_id(db, setup_users_db.id) == [db_api_key]
    assert get_db_api_key(db, setup_users_db.id, "Trading212") == db_api_key

    old_api_key = str(db_api_key.api_key)

    new_db_api_key = update_db_api_key(
        db,
        ApiKeyUpdate(
            broker_name="Trading212",
            api_key="NotARealApiKey",
            private_key="NotARealApiKey"
        ),
        generate_secret_key,
        setup_users_db.id
    )

    assert not new_db_api_key.api_key == old_api_key

    delete_db_api_key(
        db,
        ApiKeyDelete(
            broker_name="Trading212",
        ),
        setup_users_db.id
    )

    assert get_db_api_keys(db) == []



