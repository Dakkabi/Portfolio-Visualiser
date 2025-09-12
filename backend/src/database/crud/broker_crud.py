import json
import os.path

from sqlalchemy.orm import Session

from backend.src.database.models.broker_model import Broker
from backend.src.schemas.models.broker_schema import BrokerCreate

SUPPORTED_BROKERS_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "supported_brokers.json")

def get_db_broker(db: Session, broker_name: str) -> Broker | None:
    """Return a broker's name if it exists in the database, None otherwise."""
    return db.query(Broker).filter(Broker.name == broker_name).first()

def get_db_brokers(db: Session) -> list[type[Broker]]:
    """Return a list of all supported brokers in the database."""
    return db.query(Broker).all()

def create_db_broker(db: Session, broker: BrokerCreate) -> Broker:
    """Add a new broker name to the database.

    :param db: The database session.
    :param broker: The broker fields to insert.
    :return: The new broker.
    """
    db_broker = Broker(
        name=broker.name,
        type=broker.type,
        private_key_required=broker.private_key_required,
        rate_limit=broker.rate_limit,
    )
    db.add(db_broker)
    db.commit()
    db.refresh(db_broker)
    return db_broker

def read_file_into_broker_table(db: Session, file_path: str = None):
    """Read a json file into the broker's table.

    :param db: The database session.
    :param file_path: The path to the file to read, default to SUPPORTED_BROKERS_PATH.
    :return: None
    """
    if file_path is None:
        file_path = SUPPORTED_BROKERS_PATH

    with open(file_path, "r") as f:
        brokers = json.load(f)

    for broker_name, broker_info in brokers.items():
        if get_db_broker(db, broker_name) is None:
            new_broker = BrokerCreate(
                name=broker_name,
                type=broker_info["asset_types"],
                private_key_required=broker_info["private_key_required"],
                rate_limit=broker_info["rate_limit"],
            )

            create_db_broker(db, new_broker)

