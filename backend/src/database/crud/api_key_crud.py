from sqlalchemy.orm import Session

from backend.src.core.services.auth.cryptography_service import encrypt_string, decrypt_string
from backend.src.database.models.api_key_model import ApiKey
from backend.src.schemas.models.api_key_schema import *

def get_db_api_key(db: Session, api_key: ApiKeyRead) -> ApiKey | None:
    """Return an api key record by broker name and user id, returns encrypted values."""
    return db.query(ApiKey).filter(ApiKey.brokers_name == api_key.broker_name, ApiKey.users_id == api_key.user_id).first()

def create_db_api_key(db: Session, api_key: ApiKeyCreate) -> ApiKey:
    """Create a new ApiKey record in the database, encrypting the values.

    :param db: The database session.
    :param api_key: The ApiKey record to create.
    """
    db_api_key = ApiKey(
        users_id=api_key.user_id,
        brokers_name=api_key.brokers_name,
        api_key=encrypt_string(api_key.api_key),
        private_key=encrypt_string(api_key.private_key),
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

