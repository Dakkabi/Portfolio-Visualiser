from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.src.database.session import Base


class Broker(Base):
    __tablename__ = "brokers"

    name: Mapped[str] = mapped_column(String, primary_key=True)

    keys: Mapped["ApiKey"] = relationship(back_populates="brokers")