from typing import Optional
from payment import PaymentMethod
from shop import ShopItem, ShoppingCart
from decimal import Decimal


class Order(object):
    __slots__ = ("cart",)

    def __init__(self):
        self.cart = ShoppingCart()

    def _print_receipt(
        self, payment_method_name: str, total_cost: int, change: Optional[Decimal]
    ):
        print("-" * 30)
        for (order_item, quantity) in self:
            print(f"{order_item.name:<20}${order_item.price:.2f}(x{quantity})")
        print("-" * 30)
        print(f"{'Total:':<20}${total_cost:.2f}")
        print("-" * 30)

        print(f"\n{'Paid with:':<12}{payment_method_name}")
        if change:
            print(f"{'Change:':<12}${change:.2f}")
        print()

    def checkout(
        self, payment_method: PaymentMethod, cash_amount: Decimal = Decimal(0)
    ):
        total_cost = sum([item.price * quantity for (item, quantity) in self])

        if payment_method == PaymentMethod.CASH and cash_amount < total_cost:
            print("Not enough cash!")
            return False

        self._print_receipt(
            payment_method.name,
            total_cost,
            change=(cash_amount - total_cost)
            if payment_method == PaymentMethod.CASH
            else None,
        )

        return self.cart.clear()

    def add_to_order(self, order_item: ShopItem, quantity: int = 1):
        return self.cart.add_item(order_item, quantity)

    def remove_from_order(self, order_item: ShopItem, quantity: int = 1):
        return self.cart.remove_item(order_item, quantity)

    def display_order(self):
        print("-" * 30)
        self.cart.display_items()
        print("-" * 30)

    def __iter__(self):
        return iter(self.cart.items)
