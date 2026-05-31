# Exercise 6: Modulo Operator
# Objective: Check even or odd using %

def check_even_odd(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    remainder = number % 2
    result = "Even" if remainder == 0 else "Odd"
    print(f"{number} % 2 = {remainder}  ->  {result}")

number = 17
check_even_odd(number)
