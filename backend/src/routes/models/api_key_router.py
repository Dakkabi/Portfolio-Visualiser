from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.api_key_crud import create_db_api_key
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.api_key_schema import ApiKeySchema, ApiKeyCreate
from backend.src.services.security.authentication import get_current_active_user

api_key_router = APIRouter(
    prefix="/keys",
    tags=["API Keys"],
)

@api_key_router.post("/", response_model=ApiKeySchema)
def create_api_key_endpoint(
        api_key: ApiKeyCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    return create_db_api_key(db, api_key, current_user.id)
