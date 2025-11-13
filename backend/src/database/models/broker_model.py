from typing import List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.src.database.models.api_key_model import ApiKeys
from backend.src.database.models.portfolio_model import PortfolioCash
from backend.src.database.session import Base


class Broker(Base):
    __tablename__ = "brokers"

    name: Mapped[str] = mapped_column(String, primary_key=True, unique=True)

    api_keys: Mapped[List["ApiKeys"]] = relationship()
    portfolios_cash: Mapped[List["PortfolioCash"]] = relationship()