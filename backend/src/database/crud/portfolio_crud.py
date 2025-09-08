from sqlalchemy.orm import Session

from backend.src.database.models.portfolio_model import Portfolio
from backend.src.schemas.models.portfolio_schema import PortfolioCreate, PortfolioUpdate


def get_db_portfolio_by_user_id_and_broker_name(db: Session, user_id: int, broker_name: str):
    return db.query(Portfolio).filter_by(user_id=user_id, broker_name=broker_name).first()

def create_db_portfolio(db: Session, portfolio: PortfolioCreate, user_id: int) -> Portfolio:
    """Create a new portfolio entry in the database."""
    db_portfolio = Portfolio(
        user_id=user_id,
        portfolio={**portfolio.portfolio},
        broker_name=portfolio.broker_name,
    )
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

def update_db_portfolio(db: Session, portfolio: PortfolioUpdate, user_id: int):
    """Update an existing portfolio entry in the database."""
    db_portfolio = get_db_portfolio_by_user_id_and_broker_name (db, user_id, portfolio.broker_name)
    db_portfolio.portfolio = {**portfolio.portfolio}
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio