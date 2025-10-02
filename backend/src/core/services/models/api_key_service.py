from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.src.core.services.brokers import BROKER_REGISTRY
from backend.src.database.crud.api_key_crud import get_db_encrypted_api_key
from backend.src.database.crud.broker_crud import get_db_broker


def is_private_key_required(broker_name: str, db: Session) -> bool:
    """Return a bool indicating whether the private_key field is required for a broker."""
    db_broker = get_db_broker(db, broker_name)
    return bool(db_broker.private_key_required)

def check_broker_exists(broker_name: str, db: Session) -> None:
    """Raise an exception if a given broker name is not in the brokers table."""
    if not get_db_broker(db, broker_name):
        raise HTTPException(status_code=404, detail="Broker not found")

def check_api_key_exists(user_id: int, broker_name: str, db: Session ) -> bool:
    """Return a bool indicating whether an api_key record already exists between a user_id and a broker name."""
    return get_db_encrypted_api_key(db, user_id, broker_name) is not None

def validate_broker_api_keys(broker_name: str, api_key: str, private_key: str = None) -> bool:
    """Check if the API key values are accepted by the Broker clients."""
    return BROKER_REGISTRY[broker_name].validate_api_key(api_key, private_key)
