from pydantic import BaseModel

class ApiKeyBase(BaseModel):
    api_key: str
    private_key: str
    brokers_name: str

class UserBase(BaseModel):
    users_id: int

class ApiKeyRequest(ApiKeyBase):
    pass

class ApiKeyCreate(ApiKeyBase, UserBase):
    pass

class ApiKeyUpdate(ApiKeyCreate):
    pass

class ApiKeyRead(ApiKeyBase, UserBase):
    pass

class ApiKeySchema(ApiKeyBase, UserBase):
    pass
