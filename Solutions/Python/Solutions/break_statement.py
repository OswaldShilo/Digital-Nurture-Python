# Exercise 18: Break Statement
# Objective: Find and print the first even number in a range

def find_first_even(limit):
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer")
    for i in range(1, limit + 1):
        if i % 2 == 0:
            print(f"First even number in range(1, {limit+1}): {i}")
            break

find_first_even(10)
