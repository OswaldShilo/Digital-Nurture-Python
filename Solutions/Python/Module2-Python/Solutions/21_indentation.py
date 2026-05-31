# Exercise 21: Consistent Indentation
# Objective: Demonstrate 4-space indentation with nested if

def check_conditions(a, b):
    if a > 0:
        if b > 0:
            print("Nested")
    print("Both conditions checked.")

check_conditions(5, 10)
