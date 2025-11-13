from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.session import Base


class PortfolioCash(Base):
    __tablename__ = "portfolios_cash"

    free: Mapped[float] = mapped_column(Float)
    invested: Mapped[float] = mapped_column(Float)
    profit_and_loss: Mapped[float] = mapped_column(Float)
    result: Mapped[float] = mapped_column(Float)
    total: Mapped[float] = mapped_column(Float)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    broker_name: Mapped[str] = mapped_column(ForeignKey("brokers.name"), primary_key=True)
