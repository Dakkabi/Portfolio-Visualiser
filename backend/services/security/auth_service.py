from fastapi.security import OAuth2PasswordBearer

from backend.core.config import settings

ALGORITHM = "HS256"
SECRET_KEY = settings.JWT_SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")