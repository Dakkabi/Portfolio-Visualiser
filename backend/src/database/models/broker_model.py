from sqlalchemy import String, Enum, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.src.database.models.api_key_model import ApiKey
from backend.src.database.models.portfolio_model import Portfolio
from backend.src.database.session import Base
from backend.src.schemas.models.broker_enum import AssetType


class Broker(Base):
    __tablename__ = "brokers"

    name: Mapped[str] = mapped_column(String, primary_key=True)
    type : Mapped[list[AssetType]] = mapped_column(ARRAY(Enum(AssetType, name="asset_type")))
    private_key_required: Mapped[bool] = mapped_column(Boolean)

    api_keys: Mapped[ApiKey] = relationship(back_populates="brokers")
    portfolios: Mapped[Portfolio] = relationship(back_populates="brokers")