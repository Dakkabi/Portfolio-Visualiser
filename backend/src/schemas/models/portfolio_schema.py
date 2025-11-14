from pydantic import BaseModel

class PortfolioCashBase(BaseModel):
    free: float
    invested: float
    profit_and_loss: float
    result: float
    total: float
    broker_name: str

class PortfolioCashCreate(PortfolioCashBase):
    pass

class PortfolioCashUpdate(PortfolioCashBase):
    pass

class PortfolioCashSchema(PortfolioCashBase):
    pass