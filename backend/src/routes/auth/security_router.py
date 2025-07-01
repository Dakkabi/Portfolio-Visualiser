from fastapi import APIRouter, Depends

from backend.src.database.models.user_model import User
from backend.src.schemas.auth.security_schema import ResponseSchema, DeriveKeyRequest
from backend.src.services.auth.auth_service import get_current_user
from backend.src.services.auth.security_service import generate_key_from_password

security_router = APIRouter(
    prefix="/encryption",
    tags=["Encryption"]
)

@security_router.post("/derive-key", response_model=ResponseSchema)
def derive_key(request : DeriveKeyRequest, user : User = Depends(get_current_user)):
    """
    Derive an encryption key from a password.

    This endpoint does not mutate server-side resources, however to avoid logging the password in the url,
    we are using a query instead.

    :param request: A query schema for the password.
    :param user: The authenticated user to derive an encryption key for.

    :return: An encryption key to be stored.
    """
    return generate_key_from_password(user.id, request.password)