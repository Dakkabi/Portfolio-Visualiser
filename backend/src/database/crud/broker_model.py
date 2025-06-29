from sqlalchemy.orm import Session

from backend.src.database.models.broker_model import Broker
from backend.src.schemas.model.broker_schema import BrokerCreate

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
