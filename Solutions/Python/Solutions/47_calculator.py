# Exercise 47: Complete Calculator Program
# Objective: Robust calculator with +, -, *, / and error handling

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError
        return a / b
    else:
        raise ValueError(f"Unknown operator: '{op}'")

def main():
    try:
        a  = float(input("Enter first number  : "))
        b  = float(input("Enter second number : "))
        op = input("Enter operator (+, -, *, /): ").strip()
        result = calculate(a, b, op)
        print(f"Result: {a} {op} {b} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print(f"Error: {e}")

main()
