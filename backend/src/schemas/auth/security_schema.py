from pydantic import BaseModel


class SecurityUserPassword(BaseModel):
    password: str

class SecurityUserSecretKey(BaseModel):
    secret_key: str