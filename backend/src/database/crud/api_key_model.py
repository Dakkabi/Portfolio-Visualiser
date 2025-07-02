from sqlalchemy.orm import Session

from backend.src.database.models.api_key_model import ApiKey
from backend.src.database.models.user_model import User
from backend.src.schemas.model.api_key_schema import ApiKeyCreate, ApiKeyUpdate, ApiKeyDelete
from backend.src.services.auth.security_service import encrypt_data

def get_api_keys(db : Session):
    return db.query(ApiKey).all()

def get_api_key(db: Session, user_id: int, broker_name: str):
    return db.query(ApiKey).filter_by(user_id=user_id, broker_name=broker_name).first()

def create_api_key(db: Session, new_api_key: ApiKeyCreate, current_user: User):
    db_api_key = ApiKey(
        api_key=encrypt_data(new_api_key.api_key, new_api_key.secret_key),
        private_key=encrypt_data(new_api_key.private_key, new_api_key.secret_key),
        user_id=current_user.id,
        broker_name=new_api_key.broker_name
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

def update_api_key(db : Session, new_api_key: ApiKeyUpdate, current_user: User):
    record = db.query(ApiKey).filter_by(
        user_id=current_user.id,
        broker_name=new_api_key.broker_name
    ).first()

    record.api_key = encrypt_data(new_api_key.api_key, new_api_key.secret_key)
    record.private_key = encrypt_data(new_api_key.private_key, new_api_key.secret_key)

    db.commit()
    db.refresh(record)
    return record

def delete_api_key(db: Session, api_key: ApiKeyDelete, current_user: User):
    record = get_api_key(db, current_user.id, api_key.broker_name)
    db.delete(record)
    db.commit()
    db.refresh(record)
    return record