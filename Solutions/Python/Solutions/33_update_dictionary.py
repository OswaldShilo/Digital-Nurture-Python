# Exercise 33: Update Dictionary
# Objective: Merge employee details from two dictionaries using .update()

def merge_employee_data(base, updates):
    if not isinstance(base, dict) or not isinstance(updates, dict):
        raise TypeError("Both inputs must be dictionaries")
    base.update(updates)
    print("Updated Employee Data:")
    for key, value in base.items():
        print(f"  {key}: {value}")
    return base

employee = {"name": "Alice", "department": "Engineering"}
extra    = {"salary": 75000, "location": "New York"}
merge_employee_data(employee, extra)
