from fastapi import APIRouter, Depends, HTTPException

from backend.src.core.services.auth.auth_service import get_current_active_user
from backend.src.core.services.brokers import BROKER_REGISTRY
from backend.src.database.crud.api_key_crud import *
from backend.src.database.crud.broker_crud import get_db_broker
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.api_key_schema import *

api_key_router = APIRouter(
    prefix="/keys",
    tags=["API Keys"]
)

def get_valid_api_key(brokers_name: str, user_id: int, db: Session) -> ApiKey | HTTPException:
    """Check that request parameters are valid, if so return the db record, else raise an HTTPException."""
    if get_db_broker(db, brokers_name) is None:
        raise HTTPException(
            status_code=404,
            detail="Broker not found"
        )

    db_api_key = get_db_encrypted_api_key(db, user_id, brokers_name)
    if db_api_key is None:
        raise HTTPException(
            status_code=404,
            detail="API key not found"
        )

    return db_api_key

def check_api_key_values_are_valid(brokers_name: str, api_key: str, private_key: str = None) -> bool | HTTPException:
    """Check if the API key values are accepted by the Broker clients, else raise an HTTPException."""
    return BROKER_REGISTRY[brokers_name].validate_api_key(api_key, private_key)

@api_key_router.get("/{brokers_name}", response_model=ApiKeySchema)
def api_key_get_by_brokers_name(
        brokers_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Fetch api key value(s) by brokers name, if exists."""
    db_api_key = get_valid_api_key(brokers_name, current_user.id, db)
    return db_api_key

@api_key_router.post("/", response_model=ApiKeySchema)
def api_key_post(
        api_key: ApiKeyRequest,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Create a new API key record in the database."""
    try:
        db_api_key = get_valid_api_key(api_key.brokers_name, current_user.id, db)
        raise HTTPException(
            status_code=409,
            detail="API key already exists"
        )

    except HTTPException as e:
        if e.detail == "API key not found":
            pass
        else:
            raise

    check_api_key_values_are_valid(api_key.brokers_name, api_key.api_key, api_key.private_key)

    api_key_create = ApiKeyCreate(
        api_key=api_key.api_key,
        private_key=api_key.private_key,
        users_id=current_user.id,
        brokers_name=api_key.brokers_name
    )
    return create_db_api_key(db, api_key_create)

@api_key_router.put("/", response_model=ApiKeySchema)
def api_key_put(
        api_key: ApiKeyRequest,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Update an existing ApiKey record in the database."""

    # More of a check, if db_api_key is returned, it exists, therefore ApiKeyRequest parameters are valid.
    get_valid_api_key(api_key.brokers_name, current_user.id, db)
    check_api_key_values_are_valid(api_key.brokers_name, api_key.api_key, api_key.private_key)

    api_key_update = ApiKeyUpdate(
        api_key=api_key.api_key,
        private_key=api_key.private_key,
        users_id=current_user.id,
        brokers_name=api_key.brokers_name
    )
    return update_db_api_key(db, api_key_update)

@api_key_router.delete("/{brokers_name}", response_model=ApiKeySchema)
def api_key_delete(
        brokers_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Delete an ApiKey record."""

    # More of a check, if db_api_key is returned, it exists and therefore is valid.
    get_valid_api_key(brokers_name, current_user.id, db)
    return delete_db_api_key(db, current_user.id, brokers_name)