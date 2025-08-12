from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

from backend.src.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db() -> Generator[Session]:
    """Create a database session, useful for dependency injection.

    :return: A bound session to the sqlalchemy engine.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()