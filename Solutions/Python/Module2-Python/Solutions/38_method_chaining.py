# Exercise 38: Method Chaining
# Objective: Set salary and apply raise using method chaining (return self)

class Employee:
    def __init__(self, name):
        self.name   = name
        self.salary = 0

    def set_salary(self, amount):
        if amount <= 0:
            raise ValueError("Salary must be positive")
        self.salary = amount
        return self

    def apply_raise(self, percent):
        if percent <= 0:
            raise ValueError("Raise percent must be positive")
        self.salary *= (1 + percent / 100)
        return self

    def display(self):
        print(f"Employee : {self.name}")
        print(f"Salary   : Rs.{self.salary:.2f}")
        return self

Employee("Alice").set_salary(70000).apply_raise(15).display()
