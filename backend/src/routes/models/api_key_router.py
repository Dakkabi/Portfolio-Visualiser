from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.api_key_crud import create_db_api_key, get_db_api_key_by_broker, update_db_api_key, \
    delete_db_api_key
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.api_key_schema import ApiKeySchema, ApiKeyCreate, ApiKeyUpdate
from backend.src.services.security.authentication import get_current_active_user

api_key_router = APIRouter(
    prefix="/keys",
    tags=["API Keys"],
)


@api_key_router.get("/{broker_name}", response_model=ApiKeySchema)
def get_api_key_by_broker_endpoint(
        broker_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db),
):
    return get_db_api_key_by_broker(db, broker_name, current_user.id)

@api_key_router.post("/", response_model=ApiKeySchema)
def create_api_key_endpoint(
        api_key: ApiKeyCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    return create_db_api_key(db, api_key, current_user.id)

@api_key_router.put("/", response_model=ApiKeySchema)
def update_api_key_endpoint(
        api_key: ApiKeyUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    return update_db_api_key(db, api_key, current_user.id)

@api_key_router.delete("/{broker_name}")
def delete_api_key_endpoint(
        broker_name: str,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    return delete_db_api_key(db, broker_name, current_user.id)