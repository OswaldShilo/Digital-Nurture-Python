# Exercise 53: Task Scheduler
# Objective: Task class with due_date sorting and overdue detection

from datetime import datetime

class Task:
    def __init__(self, name, due_date_str, priority):
        self.name     = name
        self.due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        self.priority = priority

    def is_overdue(self):
        return self.due_date < datetime.now()

    def __str__(self):
        status = "OVERDUE" if self.is_overdue() else "Pending"
        return (f"{self.due_date.date()}  [{self.priority:<6}]  "
                f"{self.name:<25}  [{status}]")

tasks = [
    Task("Submit Report",  "2025-05-10", "High"),
    Task("Team Meeting",   "2026-07-01", "Medium"),
    Task("Code Review",    "2026-06-15", "High"),
    Task("Update Docs",    "2025-03-01", "Low"),
    Task("Deploy v2.0",    "2026-08-20", "High"),
]

sorted_tasks = sorted(tasks, key=lambda t: t.due_date)
overdue      = [t for t in sorted_tasks if t.is_overdue()]

print("Task Schedule (sorted by due date):")
print("-" * 60)
for task in sorted_tasks:
    print(task)

print(f"\nOverdue Tasks: {len(overdue)}")
for task in overdue:
    print(f"  !! {task.name}")
