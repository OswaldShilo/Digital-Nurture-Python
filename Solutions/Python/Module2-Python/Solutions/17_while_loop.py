# Exercise 17: While Loop
# Objective: Countdown from 5 to 1 using while

def countdown(count):
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")
    print("Countdown:")
    while count > 0:
        print(count)
        count -= 1
    print("Go!")

countdown(5)
