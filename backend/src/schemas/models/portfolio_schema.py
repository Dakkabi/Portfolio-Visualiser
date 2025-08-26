from pydantic import BaseModel

class User(BaseModel):
    id: int

class CashBase(BaseModel):
    total: float

class PortfolioBase(BaseModel):
    Cash: CashBase

class PortfolioCreate(PortfolioBase, User):
    pass

class PortfolioUpdate(PortfolioBase, User):
    pass

class PortfolioSchema(PortfolioBase):
    pass

