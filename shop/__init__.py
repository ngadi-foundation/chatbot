from .shop_item import ShopItem
from .shopping_basket import ShoppingCart
import types

shop_items = types.MappingProxyType(
    dict(
        hammer=ShopItem(price="9.99", name="Hammer"),
        tape_measure=ShopItem(price=5, name="Tape Measure"),
        utility_knife=ShopItem(price=5, name="Utility Knife"),
        screw_driver=ShopItem(price="3.50", name="Screw Driver"),
        circular_saw=ShopItem(price="19.99", name="Circular Saw"),
        chisel=ShopItem(price="4.99", name="Chisel"),
        hand_plane=ShopItem(price="39.87", name="Hand Plane"),
        metal_detector=ShopItem(price="24.88", name="Metal Detector"),
        shop_vac=ShopItem(price="89.99", name="Shop Vaccum"),
        power_drill=ShopItem(price="67.80", name="Power Drill"),
    )
)
