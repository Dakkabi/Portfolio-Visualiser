from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    user_id: int
    broker_name: str

class ApiKeySchema(ApiKeyBase):
    pass

class ApiKeyCreate(ApiKeyBase):
    api_key: str
    private_key: str
