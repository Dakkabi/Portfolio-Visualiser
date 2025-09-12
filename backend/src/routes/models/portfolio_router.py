from fastapi import APIRouter, Depends, HTTPException

from backend.src.core.services.auth.auth_service import get_current_active_user
from backend.src.core.services.models.portfolio_service import create_or_update_portfolio
from backend.src.database.crud.portfolio_crud import *
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.portfolio_schema import PortfolioSchema

portfolio_router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

@portfolio_router.get("/{broker_name}", response_model=PortfolioSchema)
def portfolio_get_broker(
        broker_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Get the portfolio information for a broker."""
    return create_or_update_portfolio(db, broker_name, current_user.id)


@portfolio_router.get("/total", response_model=PortfolioSchema)
def portfolio_get_total(
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Get the total value of all portfolio's the user has connected."""
    db_portfolio_list = get_db_portfolio_by_user_id(db, current_user.id)

    if db_portfolio_list is None:
        raise HTTPException(status_code=404, detail="User has no Portfolio(s)")

    portfolio = Portfolio.empty()
    for db_portfolio in db_portfolio_list:
        portfolio += Portfolio.from_dict(db_portfolio.portfolio)

    return portfolio