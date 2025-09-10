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

def is_private_key_required(broker_name: str, db: Session) -> bool:
    """Return a bool indicating whether the private_key field is required for a broker."""
    db_broker = get_db_broker(db, broker_name)
    return bool(db_broker.private_key_required)

def check_broker_exists(broker_name: str, db: Session) -> None:
    """Raise an exception if a given broker name is not in the brokers table."""
    if not get_db_broker(db, broker_name):
        raise HTTPException(status_code=404, detail="Broker not found")

def check_api_key_exists(user_id: int, broker_name: str, db: Session ) -> bool:
    """Return a bool indicating whether an api_key record already exists between a user_id and a broker name."""
    return get_db_encrypted_api_key(db, user_id, broker_name) is not None

def validate_broker_api_keys(broker_name: str, api_key: str, private_key: str = None) -> bool:
    """Check if the API key values are accepted by the Broker clients."""
    return BROKER_REGISTRY[broker_name].validate_api_key(api_key, private_key)

@api_key_router.get("/", response_model=list[ApiKeySchema])
def api_key_get(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    """Return a list of all API Keys that belong to the user."""
    return get_db_api_keys(db, current_user.id)

@api_key_router.get("/{broker_name}", response_model=ApiKeySchema)
def api_key_get_by_broker_name(
        broker_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Fetch api key value(s) by brokers name, if exists."""
    check_broker_exists(broker_name, db)
    if not check_api_key_exists(current_user.id, broker_name, db):
        raise HTTPException(status_code=404, detail="API Key not found for broker")

    return get_db_api_key(db, current_user.id, broker_name)

@api_key_router.post("/", response_model=ApiKeySchema)
def api_key_post(
        api_key: ApiKeyCreate,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Create a new API key record in the database."""
    if check_api_key_exists(current_user.id, api_key.broker_name, db): raise HTTPException(status_code=409, detail="API key(s) already exists")
    check_broker_exists(api_key.broker_name, db)
    validate_broker_api_keys(api_key.broker_name, api_key.api_key, api_key.private_key)

    if not is_private_key_required(api_key.broker_name, db): api_key.private_key = None

    return create_db_api_key(db, api_key, current_user.id)

@api_key_router.put("/", response_model=ApiKeySchema)
def api_key_put(
        api_key: ApiKeyUpdate,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Update an existing ApiKey record in the database."""

    check_broker_exists(api_key.broker_name, db)

    if not check_api_key_exists(current_user.id, api_key.broker_name, db): raise HTTPException(status_code=404, detail="No such API Key exists in table")

    if not is_private_key_required(api_key.broker_name, db): api_key.private_key = None
    validate_broker_api_keys(api_key.broker_name, api_key.api_key, api_key.private_key)

    return update_db_api_key(db, api_key, current_user.id)

@api_key_router.delete("/{broker_name}", response_model=ApiKeySchema)
def api_key_delete(
        broker_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Delete an ApiKey record."""

    check_broker_exists(broker_name, db)
    if not check_api_key_exists(current_user.id, broker_name, db): raise HTTPException(status_code=404, detail="No such API Key exists in table")

    return delete_db_api_key(db, current_user.id, broker_name)
