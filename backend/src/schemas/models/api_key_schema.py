from pydantic import BaseModel

class ApiKeyBase(BaseModel):
    api_key: str
    private_key: str | None = None
    broker_name: str

class ApiKeyCreate(ApiKeyBase):
    pass

class ApiKeyUpdate(ApiKeyCreate):
    pass

class ApiKeyRead(ApiKeyBase):
    pass

class ApiKeySchema(ApiKeyBase):
    pass
