from sqlalchemy.orm import Session

from backend.src.core.utils.secrets import encrypt_api_key, decrypt_api_key, maybe_decrypt_api_key, \
    maybe_encrypt_api_key
from backend.src.database.models.api_key_model import ApiKeys
from backend.src.schemas.models.api_key_schema import ApiKeyCreate, ApiKeyUpdate, ApiKeyBase


def get_db_encrypted_api_key_by_broker(db: Session, broker_name: str, user_id: int):
    """Return the encrypted api_key row using the user_id and broker_name candidate keys."""
    return db.query(ApiKeys).filter_by(broker_name=broker_name, user_id=user_id).first()

def get_db_api_key_by_broker(db: Session, broker_name: str, user_id: int):
    """Return the decrypted api_key row using the user_id and broker_name candidate keys."""
    db_api_key = get_db_encrypted_api_key_by_broker(db, broker_name, user_id)
    if not db_api_key:
        return None

    # Need to create a copy to avoid commiting decryption changes to the DB.
    db_api_key_copy = ApiKeyBase(
        broker_name=str(db_api_key.broker_name),
        api_key=str(db_api_key.api_key),
        secret_key=str(db_api_key.secret_key),
    )
    db_api_key_copy.api_key = decrypt_api_key(db_api_key_copy.api_key)
    db_api_key_copy.secret_key = maybe_decrypt_api_key(db_api_key_copy.secret_key)
    return db_api_key_copy

def create_db_api_key(db: Session, api_key: ApiKeyCreate, user_id: int):
    """Create a new API Key into the table, encrypting the Api Key and additional Secret Key."""
    db_api_key = ApiKeys(
        api_key=encrypt_api_key(api_key.api_key),
        secret_key=maybe_encrypt_api_key(api_key.secret_key),
        broker_name=api_key.broker_name,
        user_id=user_id,
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

def update_db_api_key(db: Session, api_key: ApiKeyUpdate, user_id: int):
    """Update an api_key row in the database."""
    db_api_key = get_db_encrypted_api_key_by_broker(db, broker_name=api_key.broker_name, user_id=user_id)
    if db_api_key:
        db_api_key.api_key = encrypt_api_key(api_key.api_key)
        db_api_key.secret_key = maybe_encrypt_api_key(api_key.secret_key)
        db.commit()
        db.refresh(db_api_key)
    return db_api_key

def delete_db_api_key(db: Session, broker_name: str, user_id: int):
    """Delete an api_key row in the database."""
    db_api_key = get_db_encrypted_api_key_by_broker(db, broker_name, user_id)
    if db_api_key:
        db.delete(db_api_key)
        db.commit()
