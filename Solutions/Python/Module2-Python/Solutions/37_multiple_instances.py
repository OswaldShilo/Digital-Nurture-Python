# Exercise 37: Multiple Instances
# Objective: Create an employee roster using multiple class instances

class Employee:
    def __init__(self, name, department, salary):
        self.name       = name
        self.department = department
        self.salary     = salary

    def display(self):
        print(f"  {self.name:<18} | {self.department:<15} | Rs.{self.salary}")

emp1 = Employee("Alice Johnson", "Engineering", 90000)
emp2 = Employee("Bob Smith",     "Marketing",   65000)
emp3 = Employee("Carol White",   "HR",          58000)

print(f"{'Name':<18} | {'Department':<15} | Salary")
print("-" * 48)
for emp in [emp1, emp2, emp3]:
    emp.display()
