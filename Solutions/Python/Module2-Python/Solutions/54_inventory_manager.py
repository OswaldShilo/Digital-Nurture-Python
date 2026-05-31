# Exercise 54: Inventory Manager
# Objective: Product hierarchy with inheritance + low-stock alerts using sets

class Product:
    def __init__(self, pid, name, price, stock):
        self.pid   = pid
        self.name  = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"[{self.pid}] {self.name:<22} Rs.{self.price:<8} Stock: {self.stock}"

class Perishable(Product):
    def __init__(self, pid, name, price, stock, expiry_days):
        super().__init__(pid, name, price, stock)
        self.expiry_days = expiry_days

    def __str__(self):
        return super().__str__() + f" | Expires in: {self.expiry_days}d"

class Electronics(Product):
    def __init__(self, pid, name, price, stock, warranty_years):
        super().__init__(pid, name, price, stock)
        self.warranty_years = warranty_years

    def __str__(self):
        return super().__str__() + f" | Warranty: {self.warranty_years}yr"

class Inventory:
    LOW_STOCK = 5

    def __init__(self):
        self.products  = {}
        self.low_stock = set()

    def add(self, product):
        self.products[product.pid] = product
        if product.stock <= self.LOW_STOCK:
            self.low_stock.add(product.pid)

    def summary(self):
        print("Inventory Summary:")
        print("-" * 62)
        for p in self.products.values():
            print(f"  {p}")
        print(f"\nLow Stock Alerts ({len(self.low_stock)} items):")
        for pid in self.low_stock:
            print(f"  !! {self.products[pid].name}")

inv = Inventory()
inv.add(Perishable("P001",  "Milk 1L",       45,   3, 5))
inv.add(Perishable("P002",  "Bread Loaf",    35,  12, 3))
inv.add(Electronics("E001", "USB Keyboard", 850,   7, 1))
inv.add(Electronics("E002", "Webcam HD",   1200,   2, 2))
inv.summary()
