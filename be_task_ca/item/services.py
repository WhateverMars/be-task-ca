from typing import List

from .model import Item
from .schema import AllItemsRepsonse, CreateItemRequest, CreateItemResponse


class ItemNotFoundError(Exception):
    pass


class ItemAlreadyExistsError(Exception):
    pass


class ItemService:
    def __init__(self, item_repository):
        self.item_repository = item_repository

    def find_item_by_id(self, item_id):
        item = self.item_repository.find_item_by_id(item_id)
        if not item:
            raise ItemNotFoundError("Item not found")
        return item

    def create_item(self, item: CreateItemRequest) -> CreateItemResponse:
        search_result = self.item_repository.find_item_by_name(item.name)
        if search_result is not None:
            raise ItemAlreadyExistsError("Item with this name already exists")

        new_item = Item(
            name=item.name,
            description=item.description,
            price=item.price,
            quantity=item.quantity,
        )

        self.item_repository.save_item(new_item)
        return self._model_to_schema(new_item)

    def get_all(self) -> List[CreateItemResponse]:
        item_list = self.item_repository.get_all_items()
        return AllItemsRepsonse(items=list(map(self._model_to_schema, item_list)))

    def _model_to_schema(self, item: Item) -> CreateItemResponse:
        return CreateItemResponse(
            id=item.id,
            name=item.name,
            description=item.description,
            price=item.price,
            quantity=item.quantity,
        )
