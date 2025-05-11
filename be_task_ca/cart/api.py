from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from ..common import get_db
from .schema import AddToCartRequest
from .services import CartService
from .repository import CartRepository
from ..user.repository import UserRepository
from ..item.repository import ItemRepository

cart_router = APIRouter(
    prefix="/users/{user_id}/cart",
    tags=["cart"],
)


def get_cart_service(db: Session = Depends(get_db)):
    cart_repository = CartRepository(db)
    user_repository = UserRepository(db)
    item_repository = ItemRepository(db)
    return CartService(cart_repository, user_repository, item_repository)


@cart_router.post("")
async def add_item_to_cart(
    user_id: UUID,
    cart_item: AddToCartRequest,
    cart_service: CartService = Depends(get_cart_service),
):
    try:
        return cart_service.add_item(user_id, cart_item)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )


@cart_router.get("")
async def get_cart(
    user_id: UUID,
    cart_service: CartService = Depends(get_cart_service)
):
    try:
        return cart_service.get_cart(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=404, detail=str(e)
        )
