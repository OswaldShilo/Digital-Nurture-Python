# Exercise 24: All Import
# Objective: Use from math import * and demonstrate multiple functions

from math import *

def math_demo(value):
    if value < 0:
        raise ValueError("Value must be non-negative for sqrt")
    print(f"Value  : {value}")
    print(f"sqrt   : {sqrt(value):.4f}")
    print(f"pow(2) : {pow(value, 2):.4f}")
    print(f"pi     : {pi:.6f}")
    print(f"floor  : {floor(value)}")
    print(f"ceil   : {ceil(value)}")

math_demo(16)
