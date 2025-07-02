from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pycparser.c_ast import Return
from sqlalchemy.orm import Session

from backend.src.database.crud.api_key_model import create_api_key, get_api_keys, get_api_keys_by_user_id, get_api_key, \
    delete_db_api_key
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.model.api_key_schema import ApiKeySchema, ApiKeyCreate, ApiKeyAuthSchema, ApiKeyUpdate
from backend.src.services.auth.auth_service import get_current_active_user

api_key_router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)

@api_key_router.get("/", response_model=List[ApiKeyAuthSchema])
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
    db_api_key = get_api_key(db, api_key.user_id, api_key.broker_name)
    if db_api_key:
        # Masking is required as the IDE will complain otherwise
        new_api_key = ApiKeyUpdate(
            api_key=api_key.api_key,
            private_key=api_key.private_key,
            broker_name=api_key.broker_name,
            secret_key=api_key.secret_key
        )
        return update_api_key(new_api_key, db, current_user)

    return create_api_key(db, api_key, current_user)

@api_key_router.put("/")
def update_api_key(
        new_api_key: ApiKeyUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    db_api_key = get_api_key(db, new_api_key.user_id, new_api_key.broker_name)
    if not db_api_key:
        return create_api_key(db, new_api_key, current_user)

    return update_api_key(new_api_key, db, current_user)

@api_key_router.delete("/{broker_name}", response_model=ApiKeySchema)
def delete_api_key(
        broker_name: str,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    db_api_key = get_api_key(db, current_user.id, broker_name)
    if db_api_key is None:
        raise HTTPException(status_code=404, detail="API Key not found")

    return delete_db_api_key(db, db_api_key, current_user.id)