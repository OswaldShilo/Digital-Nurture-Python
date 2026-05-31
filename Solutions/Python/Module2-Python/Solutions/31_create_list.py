# Exercise 31: Create List
# Objective: Create a shopping cart list and display items

def display_cart(items):
    if not items:
        raise ValueError("Cart cannot be empty")
    print("Shopping Cart:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. Rs.{item}")
    print(f"Total: Rs.{sum(items)}")

cart = [100, 250, 75]
display_cart(cart)
