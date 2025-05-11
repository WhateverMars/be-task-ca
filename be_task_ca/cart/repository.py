from .model import CartItem


class CartRepository:
    def __init__(self, db):
        self.db = db

    def get_cart(self, user_id):
        return self.db.query(CartItem).filter(CartItem.user_id == user_id).all()

    def add_item(self, user_id, item_id, quantity: int):

        existing_item_in_cart = self.db.query(CartItem).filter(
            CartItem.user_id == user_id, CartItem.item_id == item_id
        ).first()

        if existing_item_in_cart:
            existing_item_in_cart.quantity += quantity
        else:
            new_cart_item = CartItem(
                user_id=user_id,
                item_id=item_id,
                quantity=quantity,
            )
            self.db.add(new_cart_item)

        self.db.commit()
        return self.get_cart(user_id)
