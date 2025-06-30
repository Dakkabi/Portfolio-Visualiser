from backend.src.database.crud.broker_model import get_brokers, add_broker_from_file
from backend.test.database.test_session import db

def test_add_broker_from_file(db):
    # Ensure that the db is empty before,
    # Then add brokers from file
    # Assert that it is not empty.
    assert get_brokers(db) == []
    add_broker_from_file(db)
    assert not get_brokers(db) == []