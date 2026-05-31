# Exercise 25: Parameters
# Objective: Function with parameters that adds two numbers

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}")
