from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.api_key_model import create_api_key, get_api_keys
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.model.api_key_schema import ApiKeySchema, ApiKeyCreate
from backend.src.services.auth.auth_service import get_current_active_user

api_key_router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)

@api_key_router.get("/", response_model=List[ApiKeySchema])
def get_all_api_keys(db: Session = Depends(get_db)):
    return get_api_keys(db)

@api_key_router.post("/", response_model=ApiKeySchema)
def add_api_key(
        api_key: ApiKeyCreate,
        db : Session = Depends(get_db),
        current_user: User = get_current_active_user()
):
    return create_api_key(db, api_key, current_user)