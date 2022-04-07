from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(slots=True, repr=False, frozen=True)
class ShopItem:
    price: int | float | str | Decimal
    name: str

    def __post_init__(self):
        object.__setattr__(self, "price", Decimal(self.price))

    def __repr__(self) -> str:
        return f"{self.name:<25} ${self.price:.2f}"
