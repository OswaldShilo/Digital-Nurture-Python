# Exercise 26: Multiple Parameters
# Objective: Calculate rectangle area using two parameters

def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return length * width

area = rectangle_area(5, 3)
print(f"area(5, 3) = {area}")
