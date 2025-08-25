from sqlalchemy.orm import Session

from backend.src.core.services.auth.cryptography_service import encrypt_string, decrypt_string
from backend.src.database.models.api_key_model import ApiKey
from backend.src.schemas.models.api_key_schema import *

def get_db_api_keys(db: Session, users_id: int):
    """Return all user's API Keys"""
    db_api_keys = db.query(ApiKey).filter(ApiKey.users_id == users_id).all()
    for api_key in db_api_keys:
        api_key.api_key = decrypt_string(str(api_key.api_key))

        if api_key.private_key is not None:
            api_key.private_key = decrypt_string(str(api_key.private_key))

    return db_api_keys

def get_db_api_key(db: Session, users_id: int, brokers_name: str) -> ApiKey | None:
    """Return an api key record by broker name and user id, returns decrypted values."""
    db_api_key = get_db_encrypted_api_key(db, users_id, brokers_name)
    if db_api_key:
        db_api_key.api_key = decrypt_string(str(db_api_key.api_key))
        db_api_key.private_key = decrypt_string(str(db_api_key.private_key))

    return db_api_key

def get_db_encrypted_api_key(db: Session, users_id: int, brokers_name: str) -> ApiKey | None:
    """Return an api key record by broker name and user id, returns encrypted values."""
    return db.query(ApiKey).filter(ApiKey.brokers_name == brokers_name, ApiKey.users_id == users_id).first()

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
    db_api_key = get_db_encrypted_api_key(db, users_id, brokers_name)
    db.delete(db_api_key)
    db.commit()
    return db_api_key