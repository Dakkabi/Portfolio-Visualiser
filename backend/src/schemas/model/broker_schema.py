from pydantic import BaseModel


class BrokerBase(BaseModel):
    pass

class BrokerSchema(BaseModel):
    name: str

class BrokerCreate(BrokerSchema):
    pass