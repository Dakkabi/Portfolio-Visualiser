from fastapi import APIRouter, Depends, HTTPException

from backend.src.core.models.portfolio import build_portfolio
from backend.src.core.services.auth.auth_service import get_current_active_user
from backend.src.database.crud.api_key_crud import get_db_api_key
from backend.src.database.crud.broker_crud import get_db_broker
from backend.src.database.crud.portfolio_crud import *
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.schemas.models.portfolio_schema import PortfolioCreate, PortfolioUpdate, PortfolioSchema

portfolio_router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

# There are no POST endpoints, as this is a facade pattern, therefore it will automatically build and return a portfolio
# for a Broker, if there exists an API Key.

@portfolio_router.get("/{broker_name}", response_model=PortfolioSchema)
def portfolio_get_broker(
        broker_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    """Get the portfolio information for a broker."""
    if get_db_broker(db, broker_name) is None:
        raise HTTPException(status_code=404, detail=f"Broker '{broker_name}' not found")

    if (db_api_keys := get_db_api_key(db, current_user.id, broker_name)) is None:
        raise HTTPException(status_code=409, detail="User does not have API keys for the broker requested")

    portfolio = build_portfolio(broker_name, db_api_keys.api_key, db_api_keys.private_key)
    portfolio = portfolio.to_dict()

    if get_db_portfolio_by_user_id_and_broker_name(db, current_user.id, broker_name) is None:
        db_portfolio = PortfolioCreate(
            broker_name=broker_name,
            portfolio=portfolio,
        )
        return create_db_portfolio(db, db_portfolio, current_user.id)

    db_portfolio = PortfolioUpdate(
        broker_name=broker_name,
        portfolio=portfolio,
    )
    return update_db_portfolio(db, db_portfolio, current_user.id)