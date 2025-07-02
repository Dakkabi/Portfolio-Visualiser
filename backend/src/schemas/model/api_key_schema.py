from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    broker_name: str

class ApiKeySchema(ApiKeyBase):
    user_id : int

class ApiKeySensitive(ApiKeyBase):
    api_key: str
    private_key: str

class ApiKeySensitiveSchema(ApiKeySensitive, ApiKeySchema):
    pass

class ApiKeyCreate(ApiKeySensitive):
    pass

class ApiKeyUpdate(ApiKeySensitive):
    pass

class ApiKeyDelete(ApiKeySensitive):
    pass
