from backend.src.database.crud.broker_model import get_db_brokers, add_broker_from_file
from backend.test.database.test_session import db

def test_add_broker_from_file(db):
    # get_brokers_from_file is called on db setup

    assert not get_db_brokers(db) == []