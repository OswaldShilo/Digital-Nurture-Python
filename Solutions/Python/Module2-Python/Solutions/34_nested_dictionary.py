# Exercise 34: Nested Dictionary
# Objective: Store department-wise employee data and retrieve salary

def get_salary(data, department, name):
    if department not in data:
        print(f"Department '{department}' not found.")
        return None
    if name not in data[department]:
        print(f"Employee '{name}' not in {department}.")
        return None
    salary = data[department][name]["salary"]
    print(f"{name} ({department}) Salary: Rs.{salary}")
    return salary

departments = {
    "Engineering": {
        "Alice": {"salary": 90000, "role": "Senior Dev"},
        "Bob":   {"salary": 75000, "role": "Junior Dev"},
    },
    "Marketing": {
        "Carol": {"salary": 65000, "role": "Manager"},
    },
}

get_salary(departments, "Engineering", "Alice")
get_salary(departments, "Marketing", "Carol")
