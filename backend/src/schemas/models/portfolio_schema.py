from pydantic import BaseModel

class CashBase(BaseModel):
    total: float

class PortfolioBase(BaseModel):
    Cash: CashBase

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioUpdate(PortfolioBase):
    pass

class PortfolioSchema(PortfolioBase):
    pass

