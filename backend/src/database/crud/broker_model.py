import os

from sqlalchemy.orm import Session

from backend.src.database.models.broker_model import Broker
from backend.src.schemas.model.broker_schema import BrokerCreate


def get_brokers(db : Session):
    return db.query(Broker).all()

def get_broker(db: Session, broker_name: str):
    return db.query(Broker).filter(Broker.name == broker_name).first()

def add_broker(db : Session, broker: BrokerCreate):
    db_broker = Broker(
        name=broker.name
    )
    db.add(db_broker)
    db.commit()
    db.refresh(db_broker)
    return db_broker

def add_broker_from_file(db : Session, file_path : str = None):
    if file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "..", "core", "supported_brokers.txt")

    with open(file_path, "r") as file:
        broker_names = file.readlines()

    # Remove '/n' chars
    broker_names = [name.strip() for name in broker_names]

    for name in broker_names:
        if get_broker(db, name) is None:
            db_broker = add_broker(db, BrokerCreate(name=name))
