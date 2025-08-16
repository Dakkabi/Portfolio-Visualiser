from pydantic import BaseModel


from pydantic import BaseModel

class ApiKeyBase(BaseModel):
    api_key: str
    private_key: str
    broker_name: str

class UserBase(BaseModel):
    user_id: str

class ApiKeyRequest(ApiKeyBase):
    pass

class ApiKeyCreate(ApiKeyBase, UserBase):
    pass

class ApiKeyRead(ApiKeyBase):
    pass

class ApiKeySchema(ApiKeyBase):
    pass
