from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    broker_name: str

class ApiKeySchema(ApiKeyBase):
    user_id : int

class ApiKeySensitiveSchema(ApiKeyBase):
    api_key: str
    private_key: str

class ApiKeyCreate(ApiKeySensitiveSchema):
    secret_key: str

class ApiKeyUpdate(ApiKeyCreate):
    pass

class ApiKeyDelete(ApiKeyCreate):
    pass
