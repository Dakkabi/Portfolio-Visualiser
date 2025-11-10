from typing import Optional

from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    api_key: str
    secret_key: Optional[str] = None
    broker_name: str

class ApiKeyCreate(ApiKeyBase):
    pass

class ApiKeyUpdate(ApiKeyBase):
    pass

class ApiKeySchema(ApiKeyBase):
    pass
