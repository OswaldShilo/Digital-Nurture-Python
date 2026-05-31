# Exercise 8: Min/Max Functions
# Objective: Find highest and lowest salary using min() and max()

def salary_stats(salaries):
    if not salaries:
        raise ValueError("Salary list cannot be empty")
    if any(s < 0 for s in salaries):
        raise ValueError("Salaries must be non-negative")
    print(f"Salaries : {salaries}")
    print(f"Highest  : Rs.{max(salaries)}")
    print(f"Lowest   : Rs.{min(salaries)}")

salaries = [50000, 75000, 62000, 95000]
salary_stats(salaries)
