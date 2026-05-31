# Exercise 32: Append to List
# Objective: Add a new expense to an existing list using .append()

def add_expense(expenses, amount):
    if amount <= 0:
        raise ValueError("Expense amount must be positive")
    expenses.append(amount)
    print(f"Added Rs.{amount}. Updated expenses: {expenses}")
    return expenses

expenses = [500, 1200, 800]
add_expense(expenses, 450)
