from pydantic import BaseModel


class BrokerBase(BaseModel):
    name: str

class BrokerSchema(BrokerBase):
    pass