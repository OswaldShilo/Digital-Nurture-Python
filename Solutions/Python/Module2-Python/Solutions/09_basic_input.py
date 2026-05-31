# Exercise 9: Basic Input
# Objective: Read user name and print a greeting

def greet_user():
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    print(f"Hello, {name}! Welcome.")

greet_user()
