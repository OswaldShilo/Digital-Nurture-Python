# Exercise 30: Basic Try-Except
# Objective: Safely divide two numbers and handle ZeroDivisionError

def safe_divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result:.2f}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

safe_divide(10, 2)
safe_divide(5, 0)
