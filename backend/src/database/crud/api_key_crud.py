from sqlalchemy.orm import Session

from backend.src.core.services.auth.cryptography_service import encrypt_string, decrypt_string
from backend.src.database.models.api_key_model import ApiKey
from backend.src.schemas.models.api_key_schema import *

def get_db_api_key(db: Session, users_id: int, brokers_name: str) -> ApiKey | None:
    """Return an api key record by broker name and user id, returns decrypted values."""
    db_api_key = db.query(ApiKey).filter(ApiKey.brokers_name == brokers_name, ApiKey.users_id == users_id).first()
    if db_api_key:
        db_api_key.api_key = decrypt_string(str(db_api_key.api_key))
        db_api_key.private_key = decrypt_string(str(db_api_key.private_key))

    return db_api_key

def create_db_api_key(db: Session, api_key: ApiKeyCreate) -> ApiKey:
    """Create a new ApiKey record in the database, encrypting the values.

    :param db: The database session.
    :param api_key: The ApiKey record to create.
    """
    db_api_key = ApiKey(
        users_id=api_key.users_id,
        brokers_name=api_key.brokers_name,
        api_key=encrypt_string(api_key.api_key),
        private_key=encrypt_string(api_key.private_key),
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

def update_db_api_key(db: Session, api_key: ApiKeyUpdate) -> ApiKey:
    """Overwrite an ApiKey's values in the database, encrypting the new values."""
    db_api_key = get_db_api_key(db, api_key.users_id, api_key.brokers_name)
    db_api_key.api_key = encrypt_string(str(db_api_key.api_key))
    db_api_key.private_key = encrypt_string(str(db_api_key.private_key))
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

def delete_db_api_key(db: Session, users_id: int, brokers_name: str) -> ApiKey | None:
    """Delete an ApiKey record by broker name and user id."""
    db_api_key = get_db_api_key(db, users_id, brokers_name)
    db.delete(db_api_key)
    db.commit()
    return db_api_key