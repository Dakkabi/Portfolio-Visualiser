from pydantic import BaseModel

class PortfolioBase(BaseModel):
    broker_name: str

class PortfolioCreate(PortfolioBase):
    portfolio: dict

class PortfolioUpdate(PortfolioBase):
    portfolio: dict

class PortfolioSchema(PortfolioBase):
    portfolio: dict

