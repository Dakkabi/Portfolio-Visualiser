from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.session import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    portfolio: Mapped[dict] = mapped_column(JSON)

    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    users: Mapped["User"] = relationship(back_populates="portfolios")