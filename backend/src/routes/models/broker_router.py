from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.broker_model import get_brokers
from backend.src.database.session import get_db

broker_router = APIRouter(
    prefix="/brokers",
    tags=["Brokers"]
)

@broker_router.get("/")
def get_all_brokers(db : Session = Depends(get_db)):
    return get_brokers(db)
