# Exercise 13: If-Else
# Objective: Two-way decision — even or odd

def check_even_odd(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

num = 8
check_even_odd(num)
