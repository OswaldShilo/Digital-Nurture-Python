# Exercise 19: Continue Statement
# Objective: Sum only odd numbers using continue to skip evens

def sum_odd_numbers(limit):
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer")
    total = 0
    for i in range(limit):
        if i % 2 == 0:
            continue
        total += i
    print(f"Sum of odd numbers in range(0, {limit}): {total}")

sum_odd_numbers(10)
