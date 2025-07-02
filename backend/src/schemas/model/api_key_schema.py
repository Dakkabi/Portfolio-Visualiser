from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    broker_name: str

class ApiKeySchema(ApiKeyBase):
    user_id : int

class ApiKeyAuthSchema(ApiKeySchema):
    encrypted_api_key: str
    encrypted_private_key: str

class ApiKeyCreate(ApiKeyBase):
    api_key: str
    private_key: str
    secret_key: str

class ApiKeyUpdate(ApiKeyCreate):
    pass

class ApiKeyDelete(ApiKeyCreate):
    pass
