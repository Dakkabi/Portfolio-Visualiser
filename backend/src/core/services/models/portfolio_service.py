from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.src.core.models.portfolio import build_portfolio
from backend.src.database.crud.api_key_crud import get_db_api_key
from backend.src.database.crud.broker_crud import get_db_broker
from backend.src.database.crud.portfolio_crud import get_db_portfolio_by_user_id_and_broker_name, create_db_portfolio, \
    update_db_portfolio
from backend.src.schemas.models.portfolio_schema import PortfolioCreate, PortfolioUpdate


def create_or_update_portfolio(
        db: Session,
        broker_name: str,
        user_id: int
):
    """Create or update a stored portfolio from the database, with a given broker.

    :param db: The database session
    :param broker_name: The name of the broker
    :param user_id: The id of the user
    """
    if get_db_broker(db, broker_name) is None:
        raise HTTPException(status_code=404, detail=f"Broker '{broker_name}' not found")

    if (db_api_keys := get_db_api_key(db, user_id, broker_name)) is None:
        raise HTTPException(status_code=409, detail="User does not have API keys for the broker requested")

    current_portfolio = get_db_portfolio_by_user_id_and_broker_name(db, user_id, broker_name)
    new_portfolio = build_portfolio(broker_name, db_api_keys.api_key, db_api_keys.private_key).to_dict()

    if current_portfolio is None:
        db_portfolio = PortfolioCreate(
            broker_name=broker_name,
            portfolio=new_portfolio,
        )
        return create_db_portfolio(db, db_portfolio, user_id)

    db_portfolio = PortfolioUpdate(
        broker_name=broker_name,
        portfolio=new_portfolio,
    )
    return update_db_portfolio(db, db_portfolio, user_id)