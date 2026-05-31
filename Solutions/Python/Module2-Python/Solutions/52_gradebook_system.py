# Exercise 52: Gradebook System
# Objective: Manage student grades, GPA, save/load JSON, class average

import json, os

FILE = "gradebook.json"

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_grade(self, student, grade):
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            print(f"  Invalid grade {grade} for {student}. Skipped.")
            return
        self.students.setdefault(student, []).append(grade)

    def gpa(self, student):
        grades = self.students.get(student, [])
        return round(sum(grades) / len(grades), 2) if grades else 0.0

    def class_average(self):
        all_grades = [g for grades in self.students.values() for g in grades]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0.0

    def save(self):
        with open(FILE, "w") as f:
            json.dump(self.students, f, indent=2)

    def load(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                self.students = json.load(f)

    def report(self):
        print(f"{'Student':<12} | {'Grades':<28} | GPA")
        print("-" * 50)
        for student, grades in self.students.items():
            print(f"{student:<12} | {str(grades):<28} | {self.gpa(student)}")
        print(f"\nClass Average: {self.class_average()}")

gb = GradeBook()
for name, grades in [("Alice", [85, 90, 78, 92]),
                      ("Bob",   [60, 55, 70]),
                      ("Carol", [95, 98, 100, -5, 88])]:
    for g in grades:
        gb.add_grade(name, g)

gb.save()
gb.load()
gb.report()
