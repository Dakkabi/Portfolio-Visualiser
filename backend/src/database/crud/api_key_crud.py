from sqlalchemy.orm import Session

from backend.src.core.services.auth.cryptography_service import encrypt_string, decrypt_string
from backend.src.database.models.api_key_model import ApiKey
from backend.src.schemas.models.api_key_schema import *

def get_db_api_keys(db: Session, user_id: int):
    """Return all user's API Keys"""
    db_api_keys = db.query(ApiKey).filter(ApiKey.user_id == user_id).all()
    for api_key in db_api_keys:
        api_key.api_key = decrypt_string(str(api_key.api_key))

        if api_key.private_key is not None:
            api_key.private_key = decrypt_string(str(api_key.private_key))

    return db_api_keys

def get_db_api_key(db: Session, user_id: int, broker_name: str) -> ApiKey | None:
    """Return an api key record by broker name and user id, returns decrypted values."""
    db_api_key = get_db_encrypted_api_key(db, user_id, broker_name)
    if db_api_key is None:
        return None

    db_api_key.api_key = decrypt_string(str(db_api_key.api_key))

    if db_api_key.private_key is not None:
        db_api_key.private_key = decrypt_string(str(db_api_key.private_key))

    return db_api_key

def get_db_encrypted_api_key(db: Session, user_id: int, broker_name: str) -> ApiKey | None:
    """Return an api key record by broker name and user id, returns encrypted values."""
    return db.query(ApiKey).filter(ApiKey.broker_name == broker_name, ApiKey.user_id == user_id).first()

def create_db_api_key(db: Session, api_key: ApiKeyCreate, user_id: int) -> ApiKey:
    """Create a new ApiKey record in the database, encrypting the values.

    :param db: The database session.
    :param api_key: The ApiKey record to create.
    :param user_id: The user id of the user.
    """
    db_api_key = ApiKey(
        user_id=user_id,
        broker_name=api_key.broker_name,
        api_key=encrypt_string(str(api_key.api_key)),
        private_key=encrypt_string(str(api_key.private_key)),
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

def update_db_api_key(db: Session, api_key: ApiKeyUpdate, user_id: int) -> ApiKey:
    """Overwrite an ApiKey's values in the database, encrypting the new values."""
    db_api_key = get_db_api_key(db, user_id, api_key.broker_name)
    db_api_key.api_key = encrypt_string(str(db_api_key.api_key))
    db_api_key.private_key = encrypt_string(str(db_api_key.private_key))
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

def delete_db_api_key(db: Session, user_id: int, broker_name: str) -> ApiKey | None:
    """Delete an ApiKey record by broker name and user id."""
    db_api_key = get_db_encrypted_api_key(db, user_id, broker_name)
    db.delete(db_api_key)
    db.commit()
    return db_api_key
