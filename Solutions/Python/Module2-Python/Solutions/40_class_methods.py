# Exercise 40: Class Methods
# Objective: Factory classmethod to create Employee from a formatted string

class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary_str = data.split(",")
        return cls(name.strip(), int(salary_str.strip()))

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Salary : Rs.{self.salary}")

emp = Employee.from_string("Shubh,75000")
emp.display()
