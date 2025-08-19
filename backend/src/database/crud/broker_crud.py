import os.path

from sqlalchemy.orm import Session

from backend.src.database.models.broker_model import Broker
from backend.src.schemas.models.broker_enum import AssetType
from backend.src.schemas.models.broker_schema import BrokerCreate

SUPPORTED_BROKERS_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "supported_brokers.txt")

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
        type=broker.type
    )
    db.add(db_broker)
    db.commit()
    db.refresh(db_broker)
    return db_broker

def read_file_into_broker_table(db: Session, file_path: str = None):
    """Read a file, line by line, and add it as a record to the brokers table.

    :param db: The database session.
    :param file_path: The path to the file to read, default is `/backend/src/assets/supported_brokers.txt`.
    """
    if file_path is None:
        file_path = SUPPORTED_BROKERS_PATH

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            broker_name, asset_type_list = line.split(":")
            asset_types = asset_type_list.split(",")

            if broker_name != "NAME": # Header line
                if get_db_broker(db, broker_name) is None:
                    asset_type_enum_list = []
                    for asset_type in asset_types:
                        asset_type_enum_list.append(AssetType(asset_type))

                    broker_create = BrokerCreate(
                        name=broker_name,
                        type=asset_type_enum_list
                    )

                    create_db_broker(db, broker_create)

