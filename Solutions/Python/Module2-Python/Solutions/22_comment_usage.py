# Exercise 22: Comment Usage
# Objective: Show proper documentation using meaningful comments

def calculate_total_salary(base, bonus):
    # Validate inputs are non-negative
    if base < 0 or bonus < 0:
        raise ValueError("Salary components must be non-negative")

    # Calculate total compensation
    total = base + bonus
    return total

# Define salary components
base_salary = 50000
bonus       = 10000

# Compute and display result
total_salary = calculate_total_salary(base_salary, bonus)
print(f"Base Salary  : Rs.{base_salary}")
print(f"Bonus        : Rs.{bonus}")
print(f"Total Salary : Rs.{total_salary}")
