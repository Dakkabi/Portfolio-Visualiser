from sqlalchemy.orm import Session

from backend.src.database.models.portfolio_model import Portfolio
from backend.src.schemas.models.portfolio_schema import PortfolioCreate, PortfolioUpdate


def get_db_portfolio_by_user_id(db: Session, user_id: int):
    return db.query(Portfolio).filter_by(user_id=user_id).first()

def create_db_portfolio(db: Session, data: PortfolioCreate, user_id: int) -> Portfolio:
    """Create a new portfolio entry in the database."""
    db_portfolio = Portfolio(
        users_id=user_id,
        portfolio=data.model_dump()
    )
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

def update_db_portfolio(db: Session, data: PortfolioUpdate, user_id: int):
    """Update an existing portfolio entry in the database."""
    db_portfolio = get_db_portfolio_by_user_id(db, user_id)
    db_portfolio.portfolio = data.model_dump()
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio