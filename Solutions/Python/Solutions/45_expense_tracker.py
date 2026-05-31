# Exercise 45: Expense Tracker
# Objective: Analyze current-month expenses by category using datetime

import csv
from datetime import datetime

FILE = "expenses.csv"

def create_sample_expenses():
    today = datetime.now().strftime("%Y-%m-%d")
    rows = [["date", "amount", "category"],
            [today, "1200", "Food"],
            [today, "500",  "Transport"],
            [today, "3000", "Food"],
            [today, "800",  "Entertainment"],
            ["2025-01-15", "200", "Food"]]
    with open(FILE, "w", newline="") as f:
        csv.writer(f).writerows(rows)

def analyze_expenses(filename):
    current_month = datetime.now().strftime("%Y-%m")
    totals = {}
    with open(filename, "r") as f:
        for row in csv.DictReader(f):
            if row["date"].startswith(current_month):
                cat = row["category"]
                totals[cat] = totals.get(cat, 0) + float(row["amount"])

    print(f"Expenses for {current_month}:")
    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15}: Rs.{total:.2f}")
    print(f"  {'TOTAL':<15}: Rs.{sum(totals.values()):.2f}")

create_sample_expenses()
analyze_expenses(FILE)
