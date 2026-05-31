# Exercise 48: Shopping Cart System
# Objective: CartItem + ShoppingCart classes with 18% GST receipt

GST_RATE = 0.18

class CartItem:
    def __init__(self, name, price, quantity):
        self.name     = name
        self.price    = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item.name} x{item.quantity} @ Rs.{item.price}")
        return self

    def remove_item(self, name):
        self.items = [i for i in self.items if i.name != name]
        print(f"Removed: {name}")
        return self

    def calculate_total(self):
        return sum(i.subtotal() for i in self.items)

    def print_receipt(self):
        print("\n" + "=" * 36)
        print(f"{'RECEIPT':^36}")
        print("=" * 36)
        for item in self.items:
            print(f"{item.name:<20} Rs.{item.subtotal():>7.2f}")
        subtotal = self.calculate_total()
        gst      = subtotal * GST_RATE
        total    = subtotal + gst
        print("-" * 36)
        print(f"{'Subtotal':<20} Rs.{subtotal:>7.2f}")
        print(f"{'GST (18%)':<20} Rs.{gst:>7.2f}")
        print(f"{'TOTAL':<20} Rs.{total:>7.2f}")
        print("=" * 36)

cart = ShoppingCart()
cart.add_item(CartItem("Laptop Bag",  1200, 1))
cart.add_item(CartItem("USB Hub",      450, 2))
cart.add_item(CartItem("Mouse Pad",    150, 3))
cart.print_receipt()
