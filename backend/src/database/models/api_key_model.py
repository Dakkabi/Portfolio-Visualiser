from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.session import Base


class ApiKeys(Base):
    __tablename__ = "api_keys"

    api_key: Mapped[str] = mapped_column(String, nullable=False)
    secret_key: Mapped[str] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    broker_name: Mapped[str] = mapped_column(ForeignKey("brokers.name"), primary_key=True)
