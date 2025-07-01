from pydantic import BaseModel

class DeriveKeyRequest(BaseModel):
    password: str

class ResponseSchema(BaseModel):
    response: str