from sqlalchemy.orm import Session

from backend.src.database.models.broker_model import Broker
from backend.src.schemas.model.broker_schema import BrokerCreate

def add_broker(db : Session, broker: BrokerCreate):
    db_broker = Broker(
        name=broker.name
    )
    db.add(db_broker)
    db.commit()
    db.refresh(db_broker)
    return db_broker