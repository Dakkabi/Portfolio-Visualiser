from sqlalchemy.orm import Session

from backend.src.schemas.model.api_key_schema import ApiKeyCreate


def create_api_key(db : Session, new_api_key : ApiKeyCreate, secret_key : bytes):
    pass