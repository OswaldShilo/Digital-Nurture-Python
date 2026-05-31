# Exercise 39: Polymorphism
# Objective: Same method work() produces different output per subclass

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working.")

class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team.")

class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing UI/UX.")

team = [Developer("Alice"), Manager("Bob"), Designer("Carol")]
for member in team:
    member.work()
