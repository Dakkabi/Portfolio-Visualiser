from sqlalchemy.orm import Session

from backend.src.database.models.api_key_model import ApiKey
from backend.src.schemas.model.api_key_schema import ApiKeyCreate
from backend.src.services.auth.security_service import encrypt_data


def create_api_key(db : Session, new_api_key : ApiKeyCreate, secret_key : bytes):
    pass