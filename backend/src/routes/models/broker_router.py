from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.broker_crud import get_db_brokers
from backend.src.database.session import get_db
from backend.src.schemas.models.broker_schema import BrokerSchema

broker_router = APIRouter(
    prefix="/brokers",
    tags=["Brokers"],
)

@broker_router.get("/", response_model=list[BrokerSchema])
def broker_get(db: Session = Depends(get_db)):
    return get_db_brokers(db)