from sqlalchemy.orm import Session

from backend.src.database.models.api_key_model import ApiKey
from backend.src.schemas.model.api_key_schema import ApiKeyCreate
from backend.src.services.auth.security_service import encrypt_data

def get_api_keys(db : Session):
    return db.query(ApiKey).all()

def get_api_key(db: Session, user_id: int, broker_name: str):
    return db.query(ApiKey).filter_by(user_id=user_id, broker_name=broker_name).first()

def create_api_key(db: Session, new_api_key: ApiKeyCreate):
    db_api_key = ApiKey(
        api_key=encrypt_data(new_api_key.api_key, new_api_key.secret_key),
        private_key=encrypt_data(new_api_key.private_key, new_api_key.secret_key),
        user_id=new_api_key.user_id,
        broker_name=new_api_key.broker_name
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key