from fastapi import Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.broker_crud import bulk_create_db_broker_from_file
from backend.src.database.session import get_db


def bulk_insert_brokers(override_file_path: str = None, db: Session = Depends(get_db)):
    bulk_create_db_broker_from_file(db, override_file_path)