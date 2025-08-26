from datetime import datetime, timezone

from sqlalchemy import JSON, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.session import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    portfolio: Mapped[dict] = mapped_column(JSON)
    last_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["User"] = relationship(back_populates="portfolios")

    brokers_name: Mapped[str] = mapped_column(ForeignKey("brokers.name"), nullable=True, unique=True)
    brokers: Mapped["Broker"] = relationship(back_populates="portfolios")
