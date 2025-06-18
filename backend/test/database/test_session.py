from backend.src.database.session import get_db, Base
import pytest
import os
from sqlalchemy.orm.session import Session
from alembic import command
from alembic.config import Config

# What the hell.
ALEMBIC_INI_PATH = os.path.join(os.path.abspath(__file__), "..", "..", "..", "..", "alembic.ini")

@pytest.fixture
def db() -> Session:
    db_session = next(get_db())

    alembic_cfg = Config(ALEMBIC_INI_PATH)
    command.upgrade(alembic_cfg, "head")

    # TODO: Find a less destructive way to implement this
    # Perhaps a separate Test Server?
    Base.metadata.drop_all(bind=db_session.bind)
    Base.metadata.create_all(bind=db_session.bind)

    yield db_session

    db_session.close()

def test_db(db):
    assert db is not None