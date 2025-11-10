from pydantic import BaseModel


class BrokerBase(BaseModel):
    name: str

class BrokerCreate(BrokerBase):
    pass

class BrokerSchema(BrokerBase):
    pass