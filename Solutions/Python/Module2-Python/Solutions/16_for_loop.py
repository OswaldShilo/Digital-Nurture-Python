# Exercise 16: For Loop Basics
# Objective: Print numbers 1-5 using range()

def print_numbers(count):
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")
    for i in range(1, count + 1):
        print(i)

print("Numbers from 1 to 5:")
print_numbers(5)
