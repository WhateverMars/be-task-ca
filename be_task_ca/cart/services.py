class UserNotFoundError(Exception):
    pass


class ItemNotFoundError(Exception):
    pass


class InsufficientStockError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class CartService:
    def __init__(self, cart_repository, user_repository, item_repository):
        self.cart_repository = cart_repository
        self.user_repository = user_repository
        self.item_repository = item_repository

    def _validate_user(self, user_id):
        user = self.user_repository.find_user_by_id(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        return user

    def _validate_item(self, item_data):
        item = self.item_repository.find_item_by_id(item_data.item_id)
        if not item:
            raise ItemNotFoundError("Item not found")
        return item

    def _validate_item_quantity(self, item, quantity: int):
        if item.quantity < quantity:
            raise InsufficientStockError("Not enough item quantity available")
        if quantity < 1:
            raise InvalidQuantityError("Item quantity must be at least 1")

    def add_item(self, user_id, item_data):
        user = self._validate_user(user_id)
        item = self._validate_item(item_data)
        self._validate_item_quantity(item, item_data.quantity)

        return self.cart_repository.add_item(user.id, item.id, item_data.quantity)

    def get_cart(self, user_id):
        user = self._validate_user(user_id)
        return self.cart_repository.get_cart(user.id)
