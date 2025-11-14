from typing import Type

from fastapi import HTTPException

from backend.src.database.crud.api_key_crud import get_db_api_key_by_broker
from backend.src.database.crud.broker_crud import get_db_broker
from backend.src.database.crud.portfolio_crud import *
from backend.src.services.api import BROKER_REGISTRY
from backend.src.services.api.abstract_broker_client import AbstractBrokerClient


def update_portfolio_cash(db: Session, user_id: int, broker_name: str):
    """Create or update a portfolio cash row in the database."""
    if not get_db_broker(db, broker_name):
        raise HTTPException(status_code=400, detail=f"Broker {broker_name} does not exist")

    db_api_key = get_db_api_key_by_broker(db, broker_name, user_id)
    if not db_api_key:
        raise HTTPException(status_code=403, detail="User does not have API key for selected broker / exchange")

    broker_cls: Type[AbstractBrokerClient] = BROKER_REGISTRY[broker_name]
    broker: AbstractBrokerClient = broker_cls(db_api_key.api_key, db_api_key.secret)
    portfolio_cash_data = broker.request_cash_data()

    if get_db_portfolio_cash(db, user_id, broker_name):
        # Portfolio already exists
        return create_db_portfolio_cash(db, portfolio_cash_data, user_id)

    return update_db_portfolio_cash(db, portfolio_cash_data, user_id)