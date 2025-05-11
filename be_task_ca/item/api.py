from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .repository import ItemRepository
from .services import ItemService

from ..common import get_db

from .schema import CreateItemRequest, CreateItemResponse


item_router = APIRouter(
    prefix="/items",
    tags=["item"],
)


@item_router.post("/")
async def post_item(
    item: CreateItemRequest, db: Session = Depends(get_db)
) -> CreateItemResponse:
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    try:
        return item_service.create_item(item)
    except Exception as e:
        raise HTTPException(
            status_code=409, detail=str(e)
        )


@item_router.get("/")
async def get_items(db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    try:
        return item_service.get_all()
    except Exception as e:
        raise HTTPException(
            status_code=404, detail=str(e)
        )
