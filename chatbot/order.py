from shop import ShopItem, ShoppingCart


class Order(object):
    __slots__ = ("cart",)

    def __init__(self):
        self.cart = ShoppingCart()

    def _print_receipt(self):
        for (order_item, quantity) in self:
            print(f"{order_item.name}\t\t${order_item.price:.2f}(x{quantity})")

        print(
            f"\n\nTotal: ${sum([item.price * quantity for (item, quantity) in self]):.2f}"
        )

    def checkout(self):

        self.print_receipt()
        return False

    def add_to_order(self, order_item: ShopItem, quantity: int = 1):
        return self.cart.add_item(order_item, quantity)

    def remove_from_order(self, order_item: ShopItem, quantity: int = 1):
        return self.cart.remove_item(order_item, quantity)

    def display_order(self):
        self.cart.display_items()

    def __iter__(self):
        return iter(self.cart.items)
