from pydantic import BaseModel

from backend.src.schemas.models.broker_enum import AssetType


class BrokerBase(BaseModel):
    name: str
    type: list[AssetType]
    private_key_required: bool

class BrokerCreate(BrokerBase):
    pass

class BrokerSchema(BrokerBase):
    pass