from sqlalchemy import JSON, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.core.services.time_service import epoch_now
from backend.src.database.session import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    portfolio: Mapped[dict] = mapped_column(JSON)
    order_history: Mapped[dict] = mapped_column(JSON)
    last_updated: Mapped[int] = mapped_column(Integer, default=epoch_now(), onupdate=epoch_now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["User"] = relationship(back_populates="portfolios")

    broker_name: Mapped[str] = mapped_column(ForeignKey("brokers.name"), nullable=True, unique=True)
    brokers: Mapped["Broker"] = relationship(back_populates="portfolios")
