from typing import List

from fastapi import APIRouter, Depends, HTTPException

from backend.src.database.crud.api_key_model import *
from backend.src.database.crud.broker_model import get_db_broker
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.auth.security_schema import SecurityUserSecretKey
from backend.src.schemas.model.api_key_schema import *
from backend.src.services.auth.auth_service import get_current_active_user
from backend.src.services.auth.security_service import decrypt_data
from backend.src.services.brokers.broker_registry import broker_registry

api_key_router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)

@api_key_router.get("/", response_model=List[ApiKeySensitiveSchema], description="Returns all encrypted API keys")
def get_my_api_keys(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    return get_db_api_keys_by_user_id(db, current_user.id)

@api_key_router.post("/", response_model=ApiKeySchema)
def add_api_key(
        api_key: ApiKeyCreate,
        secret_key: SecurityUserSecretKey,
        db : Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    if not get_db_broker(db, api_key.broker_name):
        raise HTTPException(status_code=404, detail="Broker not found")

    db_api_key = get_db_api_key(db, current_user.id, api_key.broker_name)
    if db_api_key:
        raise HTTPException(status_code=409, detail="Key already exists")

    api_key_verify_response = broker_registry[api_key.broker_name].verify_api_key_response()
    if api_key_verify_response:
        raise HTTPException(
            status_code=400,
            detail="Key is invalid."
        )

    return create_db_api_key(db, api_key, secret_key.secret_key, current_user.id)

@api_key_router.post("/decrypt/", response_model=List[ApiKeySensitiveSchema])
def get_all_decoded_api_keys(
        secret_key: SecurityUserSecretKey,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    response = get_db_api_keys_by_user_id(db, current_user.id)

    for schema in response:
        schema.api_key = decrypt_data(str(schema.api_key), secret_key.secret_key)
        schema.private_key = decrypt_data(str(schema.private_key), secret_key.secret_key)

    return response

@api_key_router.post("/decrypt/{broker_name}", response_model=ApiKeySensitiveSchema)
def get_decoded_api_key(
        broker_name: str,
        secret_key: SecurityUserSecretKey,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    response = get_db_api_key(db, current_user.id, broker_name)

    response.api_key = decrypt_data(str(response.api_key), secret_key.secret_key)
    response.private_key = decrypt_data(str(response.private_key), secret_key.secret_key)

    return response

@api_key_router.put("/", response_model=ApiKeySensitiveSchema)
def update_api_key(
        new_api_key: ApiKeyUpdate,
        secret_key: SecurityUserSecretKey,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    if not get_db_broker(db, new_api_key.broker_name):
        raise HTTPException(status_code=404, detail="Broker not found")

    db_api_key = get_db_api_key(db, current_user.id, new_api_key.broker_name)
    if not db_api_key:
        raise HTTPException(status_code=404, detail="Key not found")

    api_key_verify_response = registry[new_api_key.broker_name](new_api_key.api_key)
    if api_key_verify_response:
        raise HTTPException(
            status_code=400,
            detail="Key is invalid."
        )

    return update_db_api_key(db, new_api_key, secret_key.secret_key, current_user.id)

@api_key_router.delete("/{broker_name}", response_model=ApiKeySchema)
def delete_api_key(
        broker_name: str,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    if not get_db_broker(db, broker_name):
        raise HTTPException(status_code=404, detail="Broker not found")

    db_api_key = get_db_api_key(db, current_user.id, broker_name)
    if db_api_key is None:
        raise HTTPException(status_code=404, detail="API Key not found")

    return delete_db_api_key(db, db_api_key, current_user.id)