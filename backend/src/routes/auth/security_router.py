from fastapi import APIRouter, Depends, Security

from backend.src.database.models.user_model import User
from backend.src.schemas.auth.security_schema import SecurityUserPassword
from backend.src.services.auth.auth_service import get_current_active_user
from backend.src.services.auth.security_service import generate_key_from_password

security_router = APIRouter(
    prefix="/encryption",
    tags=["Encryption"]
)

@security_router.post("/derive-key")
def derive_key(password: SecurityUserPassword, user: User = Depends(get_current_active_user)):
    return generate_key_from_password(user.id, password.password)