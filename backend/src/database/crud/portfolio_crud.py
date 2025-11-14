from sqlalchemy.orm import Session

from backend.src.database.models.portfolio_model import PortfolioCash
from backend.src.schemas.models.portfolio_schema import PortfolioCashCreate, PortfolioCashUpdate


def get_db_portfolio_cash(db: Session, user_id: int, broker_name: str):
    """Return a row from the PortfolioCash table using the composite keys."""
    return db.query(PortfolioCash).filter_by(user_id=user_id, broker_name=broker_name).first()

def create_db_portfolio_cash(db: Session, portfolio_cash: PortfolioCashCreate, user_id: int):
    """Create a new entry into the PortfolioCash table."""
    db_portfolio_cash = PortfolioCash(
        free=portfolio_cash.free,
        invested=portfolio_cash.invested,
        profit_and_loss=portfolio_cash.profit_and_loss,
        result=portfolio_cash.result,
        total=portfolio_cash.total,
        broker_name=portfolio_cash.broker_name,
        user_id=user_id
    )
    db.add(db_portfolio_cash)
    db.commit()
    db.refresh(db_portfolio_cash)
    return db_portfolio_cash

def update_db_portfolio_cash(db: Session, portfolio_cash: PortfolioCashUpdate, user_id: int):
    """Update a row from the PortfolioCash table."""
    db_portfolio_cash = get_db_portfolio_cash(db, user_id, portfolio_cash.broker_name)
    if db_portfolio_cash:
        db_portfolio_cash.free = portfolio_cash.free
        db_portfolio_cash.invested = portfolio_cash.invested
        db_portfolio_cash.profit_and_loss = portfolio_cash.profit_and_loss
        db_portfolio_cash.result = portfolio_cash.result
        db_portfolio_cash.total = portfolio_cash.total

    return db_portfolio_cash


