import os.path

from sqlalchemy.orm import Session

from backend.src.database.models.broker_model import Broker

SUPPORTED_BROKERS_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "supported_brokers.txt")

def get_db_broker(db: Session, broker_name: str) -> Broker | None:
    return db.query(Broker).filter(Broker.name == broker_name).first()

def create_db_broker(db: Session, broker_name: str) -> Broker:
    """Add a new broker name to the database.

    :param db: The database session.
    :param broker_name: The name of the broker.
    :return: The new broker.
    """
    db_broker = Broker(
        name=broker_name
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
            broker_name = line.strip()
            if get_db_broker(db, broker_name) is None:
                create_db_broker(db, broker_name)
