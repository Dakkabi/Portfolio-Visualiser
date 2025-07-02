from typing import List

from fastapi import APIRouter, Depends
from pycparser.c_ast import Return
from sqlalchemy.orm import Session

from backend.src.database.crud.api_key_model import create_api_key, get_api_keys, get_api_keys_by_user_id
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.model.api_key_schema import ApiKeySchema, ApiKeyCreate, ApiKeyAuthSchema
from backend.src.services.auth.auth_service import get_current_active_user

api_key_router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)

@api_key_router.get("/", response_model=List[ApiKeySchema])
def get_all_api_keys(db: Session = Depends(get_db)):
    return get_api_keys(db)

@api_key_router.get("/me", response_model=List[ApiKeyAuthSchema])
def get_my_api_keys(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    response = get_api_keys_by_user_id(db, current_user.id)

    for schema in response:
        # It is an ApiKey schema, not a dict
        schema.encrypted_api_key = schema.api_key
        schema.encrypted_private_key = schema.private_key

        del schema.api_key
        del schema.private_key

    return response

@api_key_router.post("/", response_model=ApiKeySchema)
def add_api_key(
        api_key: ApiKeyCreate,
        db : Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    return create_api_key(db, api_key, current_user)