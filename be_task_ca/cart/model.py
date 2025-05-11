from dataclasses import dataclass
import uuid

from sqlalchemy import ForeignKey
from be_task_ca.database import Base
from sqlalchemy.orm import Mapped, mapped_column


@dataclass
class CartItem(Base):
    __tablename__ = "cart_items"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), primary_key=True, index=True
    )
    item_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("items.id"), primary_key=True)
    quantity: Mapped[int]
