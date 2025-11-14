import os

from sqlalchemy.orm import Session

from backend.src.services.utils.path_util import get_resources_path
from backend.src.database.models.broker_model import Broker
from backend.src.schemas.models.broker_schema import BrokerCreate

def get_db_broker(db: Session, name: str):
    return db.query(Broker).filter(Broker.name == name).first()

def create_db_broker(db: Session, broker: BrokerCreate):
    db_broker = Broker(
        name=broker.name,
    )
    db.add(db_broker)
    db.commit()
    db.refresh(db_broker)
    return db_broker

def create_db_broker_from_file(db: Session, file_path: str = None):
    """Do a bulk insert for the brokers table, using a JSON file as parameters.

    :param db: The database session.
    :param file_path: The path to a given JSON file, default is /backend/resources/brokers.txt, relative to repository root.
    """
    if file_path is None:
        file_path = os.path.join(get_resources_path(), "brokers.txt")

    with open(file_path, "r") as f:
        for line in f:
            if get_db_broker(db=db, name=line.strip()):
                continue

            create_db_broker(db, BrokerCreate(name=line.strip()))