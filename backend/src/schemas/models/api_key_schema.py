from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    pass

class ApiKeyCreate(ApiKeyBase):
    user_id: int
    broker_name: str
    api_key: str
    private_key: str

class ApiKeySchema(ApiKeyBase):
    pass