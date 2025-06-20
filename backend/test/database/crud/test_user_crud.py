import pytest
from sqlalchemy.orm.session import Session
from backend.src.database.crud.user_crud import *
from backend.test.database.test_session import db

def test_create_user_and_get_user(db: Session):
    user = UserCreate(
        email="test@test.com",
        password="unhashed"
    )
    user2 = UserCreate(
        email="quick@test.com",
        password="test"
    )

    new_user = create_user(db, user)

    assert get_user(db, new_user.id) == new_user
    assert get_user_by_email(db, new_user.email) == new_user

    assert new_user.password != user.password

    assert isinstance(get_users(db), list)
    assert len(get_users(db)) == 1

    create_user(db, user2)
    assert len(get_users(db)) == 2