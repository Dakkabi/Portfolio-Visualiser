import pytest
from sqlalchemy.orm.session import Session
from backend.src.database.crud.user_crud import *
from backend.src.database.session import get_db
from backend.src.schemas.user_schema import UserCreate
from backend.test.database.test_session import db


