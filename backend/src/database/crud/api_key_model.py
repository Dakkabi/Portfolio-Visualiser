from sqlalchemy.orm import Session

from backend.src.database.models.api_key_model import ApiKey
from backend.src.database.models.user_model import User
from backend.src.schemas.model.api_key_schema import ApiKeyCreate, ApiKeyUpdate, ApiKeyDelete
from backend.src.services.auth.security_service import encrypt_data

def get_db_api_keys(db : Session):
    return db.query(ApiKey).all()

def get_db_api_key(db: Session, user_id: int, broker_name: str):
    return db.query(ApiKey).filter_by(user_id=user_id, broker_name=broker_name).first()

def get_db_api_keys_by_user_id(db : Session, user_id: int):
    return db.query(ApiKey).filter_by(user_id=user_id).all()

def create_db_api_key(
        db: Session,
        new_api_key: ApiKeyCreate,
        secret_key: str,
        user_id: int
):
    db_api_key = ApiKey(
        api_key=encrypt_data(new_api_key.api_key, secret_key),
        private_key=encrypt_data(new_api_key.private_key, secret_key),
        user_id=user_id,
        broker_name=new_api_key.broker_name
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

def update_db_api_key(
        db : Session,
        new_api_key: ApiKeyUpdate,
        secret_key: str,
        user_id: int
):
    record = db.query(ApiKey).filter_by(
        user_id=user_id,
        broker_name=new_api_key.broker_name
    ).first()

    record.api_key = encrypt_data(new_api_key.api_key, secret_key)
    record.private_key = encrypt_data(new_api_key.private_key, secret_key)

    db.commit()
    db.refresh(record)
    return record

def delete_db_api_key(db: Session, api_key: ApiKeyDelete, user_id: int):
    record = get_db_api_key(db, user_id, api_key.broker_name)
    db.delete(record)
    db.commit()
    return record