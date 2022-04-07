from dataclasses import dataclass, field
from shop import ShopItem
import itertools


@dataclass
class ShoppingCart:
    __items: list[ShopItem] = field(init=False, default_factory=list)

    def add_item(self, item: ShopItem, quantity: int = 1) -> bool:
        self.__items.extend(itertools.repeat(item, quantity))
        return True

    def remove_item(self, item: ShopItem, quantity: int = 1) -> bool:
        for _ in range(quantity):
            try:
                self.__items.remove(item)
            except ValueError:
                return False
        return True

    def display_items(self):
        if self.__items:
            for (item, count) in self.items:
                print(f"{item.name:<25} (x{count})")
            return True
        print("Your cart is empty.")
        return False

    @property
    def items(self):
        return [(item, self.__items.count(item)) for item in set(self.__items)]
