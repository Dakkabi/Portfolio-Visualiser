from sqlalchemy.orm import Session

from backend.src.schemas.model.api_key_schema import ApiKeyCreate
from backend.src.services.auth.security_service import encrypt_data


def create_api_key(db: Session, new_api_key: ApiKeyCreate, secret_key: str):
    db_api_key = ApiKeyCreate(
        api_key=encrypt_data(new_api_key.api_key, secret_key),
        private_key=encrypt_data(new_api_key.private_key, secret_key),
        user_id=new_api_key.user_id,
        broker_name=new_api_key.broker_name
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key