import pytest
from sqlalchemy.orm.session import Session
from database.crud.user_crud import *
from database.session import get_db
from schemas.user_schema import UserCreate


@pytest.fixture
def db() -> Session:
    return get_db()

def test_create_and_get_user(db):
    user = UserCreate(
        email="test@test.com",
        password="plaintext123"
    )

    create_user(next(db), user)


