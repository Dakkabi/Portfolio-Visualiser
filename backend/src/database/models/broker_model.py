from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from backend.src.database.session import Base


class Broker(Base):
    __tablename__ = "brokers"

    name: Mapped[str] = mapped_column(String, primary_key=True, unique=True)