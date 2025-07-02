from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    broker_name: str

class ApiKeySchema(ApiKeyBase):
    user_id : int

class ApiKeyCreate(ApiKeyBase):
    api_key: str
    private_key: str
    secret_key: str
