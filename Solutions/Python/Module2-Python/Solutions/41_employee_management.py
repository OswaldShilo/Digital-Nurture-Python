# Exercise 41: Employee Management System
# Objective: Classes + dictionaries + JSON file I/O

import json
import os

FILE = "emps.json"

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id     = emp_id
        self.name       = name
        self.department = department
        self.salary     = salary

    def __str__(self):
        return f"[{self.emp_id}] {self.name} | {self.department} | Rs.{self.salary}"

    def to_dict(self):
        return {"emp_id": self.emp_id, "name": self.name,
                "department": self.department, "salary": self.salary}

def save_employees(employees):
    with open(FILE, "w") as f:
        json.dump([e.to_dict() for e in employees.values()], f, indent=2)
    print(f"Saved {len(employees)} employee(s) to {FILE}")

def load_employees():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        data = json.load(f)
    return {d["emp_id"]: Employee(**d) for d in data}

employees = {
    "E001": Employee("E001", "Alice Johnson", "Engineering", 90000),
    "E002": Employee("E002", "Bob Smith",     "Marketing",   65000),
    "E003": Employee("E003", "Carol White",   "HR",          58000),
}

save_employees(employees)
loaded = load_employees()

print("\nAll Employees:")
for emp in loaded.values():
    print(" ", emp)
