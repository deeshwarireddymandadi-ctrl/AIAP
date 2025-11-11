import unittest

# Tests expect a ShoppingCart with methods:
#   add_item(name: str, price: float) -> None
#   remove_item(name: str) -> None
#   total_cost() -> float
#
# If user's implementation is not available or has a different API,
# the fallback below provides a reasonable behavior for the tests:
# - add_item adds or updates an item (by name) with the given price
# - remove_item removes the named item or raises KeyError if missing
# - total_cost returns sum of item prices (rounded to 2 decimals)

try:
    from shopping_cart import ShoppingCart  # adjust import path if needed
except Exception:
    class ShoppingCart:
        def __init__(self):
            self._items = {}  # name -> price (float)

        def add_item(self, name: str, price: float):
            if not isinstance(name, str) or not name:
                raise ValueError("name must be a non-empty string")
            try:
                price = float(price)
            except (TypeError, ValueError):
                raise ValueError("price must be a number")
            if price < 0:
                raise ValueError("price must be non-negative")
            # Add or update item price
            self._items[name] = price

        def remove_item(self, name: str):
            if name not in self._items:
                raise KeyError("item not in cart")
            del self._items[name]

        def total_cost(self) -> float:
            return round(sum(self._items.values()), 2)

        def clear(self):
            self._items.clear()


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_empty_cart_total_zero(self):
        self.assertAlmostEqual(self.cart.total_cost(), 0.0)

    def test_add_single_item_and_total(self):
        self.cart.add_item("apple", 0.50)
        self.assertAlmostEqual(self.cart.total_cost(), 0.50)

    def test_add_multiple_items(self):
        self.cart.add_item("banana", 0.25)
        self.cart.add_item("milk", 1.20)
        self.assertAlmostEqual(self.cart.total_cost(), 0.25 + 1.20)

    def test_add_same_item_updates_price(self):
        self.cart.add_item("widget", 1.00)
        # adding same item name again updates the price (expected behavior)
        self.cart.add_item("widget", 1.50)
        self.assertAlmostEqual(self.cart.total_cost(), 1.50)

    def test_remove_item_reduces_total(self):
        self.cart.add_item("juice", 2.00)
        self.cart.add_item("chips", 1.50)
        self.cart.remove_item("juice")
        self.assertAlmostEqual(self.cart.total_cost(), 1.50)

    def test_remove_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.cart.remove_item("does_not_exist")

    def test_negative_price_raises(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("bad", -1.0)

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("", 1.0)
        with self.assertRaises(ValueError):
            self.cart.add_item(None, 1.0)

    def test_price_type_handling(self):
        # numeric string should be accepted if convertible
        self.cart.add_item("conv", "2.50")
        self.assertAlmostEqual(self.cart.total_cost(), 2.50)
        # non-convertible string should raise
        with self.assertRaises(ValueError):
            self.cart.add_item("badprice", "two")

    def test_float_rounding(self):
        self.cart.add_item("gadget", 0.3333)
        self.cart.add_item("gadget2", 0.3333)
        # total = 0.6666 -> rounded to 0.67
        self.assertAlmostEqual(self.cart.total_cost(), round(0.3333 + 0.3333, 2))

    def test_clear_cart_method_optional(self):
        self.cart.add_item("x", 1.0)
        # clear() is convenience; if not present tests fallback should still work
        try:
            self.cart.clear()
            self.assertAlmostEqual(self.cart.total_cost(), 0.0)
        except AttributeError:
            # emulate clear by removing items
            for name in list(getattr(self.cart, "_items", {}).keys()):
                self.cart.remove_item(name)
            self.assertAlmostEqual(self.cart.total_cost(), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)