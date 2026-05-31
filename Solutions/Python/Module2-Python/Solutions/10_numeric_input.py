# Exercise 10: Numeric Input
# Objective: Convert input to integer and print next year's age

def next_year_age():
    raw = input("Enter your age: ").strip()
    if not raw.isdigit():
        print("Error: Please enter a valid numeric age.")
        return
    age = int(raw)
    if not (0 <= age <= 150):
        print("Error: Please enter a realistic age.")
        return
    print(f"Next year you'll be {age + 1}")

next_year_age()
