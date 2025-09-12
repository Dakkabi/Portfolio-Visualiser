from pydantic import BaseModel

class PortfolioBase(BaseModel):
    portfolio: dict

class BrokerBase(BaseModel):
    broker_name: str

class PortfolioCreate(PortfolioBase, BrokerBase):
    pass

class PortfolioUpdate(PortfolioBase, BrokerBase):
    pass

class PortfolioSchema(PortfolioBase):
    pass

