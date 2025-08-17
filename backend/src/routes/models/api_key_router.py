from fastapi import APIRouter, Depends

from backend.src.core.services.auth.auth_service import get_current_active_user
from backend.src.database.crud.api_key_crud import *
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.api_key_schema import *

api_key_router = APIRouter(
    prefix="/keys",
    tags=["API Keys"]
)

@api_key_router.get("/{brokers_name}", response_model=ApiKeySchema)
def api_key_get_by_brokers_name(
        brokers_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Fetch api key value(s) by brokers name, if exists."""
    return get_db_api_key(db, current_user.id, brokers_name)

@api_key_router.post("/", response_model=ApiKeySchema)
def api_key_post(
        api_key: ApiKeyRequest,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Create a new API key record in the database."""
    api_key_create = ApiKeyCreate(
        api_key=api_key.api_key,
        private_key=api_key.private_key,
        user_id=current_user.id,
        brokers_name=api_key.brokers_name
    )
    return create_db_api_key(db, api_key_create)