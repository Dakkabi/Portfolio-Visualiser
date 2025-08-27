from pydantic import BaseModel

class CashBase(BaseModel):
    total: float

class BrokerBase(BaseModel):
    broker_name: str

class PortfolioBase(BaseModel):
    Cash: CashBase

class PortfolioCreate(BrokerBase):
    portfolio: PortfolioBase

class PortfolioUpdate(BrokerBase):
    portfolio: PortfolioBase

class PortfolioSchema(PortfolioBase):
    pass

