from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException

from backend.src.database.crud.api_key_model import *
from backend.src.database.crud.broker_model import get_db_broker
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.model.api_key_schema import *
from backend.src.services.auth.auth_service import get_current_active_user

api_key_router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)

@api_key_router.get("/", response_model=List[ApiKeySensitiveSchema])
def get_my_api_keys(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    response = get_db_api_keys_by_user_id(db, current_user.id)

    return response

@api_key_router.post("/", response_model=ApiKeySensitiveSchema)
def add_api_key(
        api_key: ApiKeyCreate,
        db : Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    if not get_db_broker(db, api_key.broker_name):
        raise HTTPException(status_code=404, detail="Broker not found")

    db_api_key = get_db_api_key(db, current_user.id, api_key.broker_name)
    if db_api_key:
        raise HTTPException(status_code=409, detail="Key already exists")

    return create_db_api_key(db, api_key, current_user)

@api_key_router.put("/", response_model=ApiKeySensitiveSchema)
def update_api_key(
        new_api_key: ApiKeyUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    if not get_db_broker(db, new_api_key.broker_name):
        raise HTTPException(status_code=404, detail="Broker not found")

    db_api_key = get_db_api_key(db, current_user.id, new_api_key.broker_name)
    if not db_api_key:
        raise HTTPException(status_code=404, detail="Key not found")

    return update_db_api_key(db, new_api_key, current_user)

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