from sqlalchemy.orm import Session

from backend.src.core.utils.secrets import encrypt_api_key
from backend.src.database.models.api_key_model import ApiKeys
from backend.src.schemas.models.api_key_schema import ApiKeyCreate


def create_db_api_key(db: Session, api_key: ApiKeyCreate, user_id: int):
    """Create a new API Key into the table, encrypting the Api Key and additional Secret Key."""
    db_api_key = ApiKeys(
        api_key=encrypt_api_key(api_key.api_key),
        secret_key=encrypt_api_key(api_key.secret_key) if api_key.secret_key else None,
        broker_name=api_key.broker_name,
        user_id=user_id,
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

