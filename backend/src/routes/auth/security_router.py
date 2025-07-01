from fastapi import APIRouter, Depends

from backend.src.database.models.user_model import User
from backend.src.services.auth.auth_service import get_current_user
from backend.src.services.auth.security_service import generate_key_from_password

security_router = APIRouter(
    prefix="/encryption",
    tags=["Encryption"]
)

@security_router.get("/derive-key")
def derive_key(password : str, user : User = Depends(get_current_user)):
    return generate_key_from_password(user.id, password)