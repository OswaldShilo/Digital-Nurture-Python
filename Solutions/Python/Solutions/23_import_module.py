# Exercise 23: Import Standard Module
# Objective: Use math module to calculate circle area

import math

def circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * radius ** 2

radius = 7
area   = circle_area(radius)
print(f"Radius : {radius}")
print(f"Area   : {area:.2f}")
