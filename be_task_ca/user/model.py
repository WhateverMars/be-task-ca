from dataclasses import dataclass
from typing import List
import uuid

from be_task_ca.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..cart.model import CartItem


@dataclass
class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4(),
        index=True,
    )
    email: Mapped[str] = mapped_column(unique=True, index=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    hashed_password: Mapped[str]
    shipping_address: Mapped[str] = mapped_column(default=None)
    cart_items: Mapped[List["CartItem"]] = relationship()
