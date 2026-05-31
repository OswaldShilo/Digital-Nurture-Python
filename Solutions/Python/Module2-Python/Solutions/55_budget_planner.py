# Exercise 55: Budget Planner
# Objective: Monthly budget tracker with overspend alerts + matplotlib pie chart
# Install: pip install matplotlib

import matplotlib
matplotlib.use("Agg")   # non-interactive backend — saves to file
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name  = name
        self.limit = limit
        self.spent = 0.0

    def add_expense(self, amount):
        self.spent += amount
        if self.spent > self.limit:
            print(f"  WARNING: '{self.name}' exceeded budget! "
                  f"(Rs.{self.spent:.0f} / Rs.{self.limit:.0f})")

categories = {
    "Food":          Category("Food",          8000),
    "Transport":     Category("Transport",     3000),
    "Entertainment": Category("Entertainment", 2000),
    "Utilities":     Category("Utilities",     4000),
}

transactions = [
    ("Food", 1200), ("Transport", 500),  ("Food", 3000),
    ("Entertainment", 800), ("Food", 4500), ("Utilities", 3500),
    ("Transport", 3200),    ("Entertainment", 1400),
]

print("Recording expenses:")
for cat, amount in transactions:
    categories[cat].add_expense(amount)

print("\nBudget Summary:")
print(f"{'Category':<18} {'Limit':>8} {'Spent':>8} {'Status':>8}")
print("-" * 46)
for c in categories.values():
    status = "OVER" if c.spent > c.limit else "OK"
    print(f"{c.name:<18} Rs.{c.limit:>6.0f} Rs.{c.spent:>6.0f} {status:>8}")

labels = [c.name for c in categories.values()]
sizes  = [c.spent for c in categories.values()]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.set_title("Monthly Expense Breakdown")
plt.tight_layout()
plt.savefig("budget_chart.png")
print("\nPie chart saved -> budget_chart.png")
