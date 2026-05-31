# Exercise 44: CSV Data Processor
# Objective: Analyze employee salary data from CSV using list comprehension

import csv
import os

FILE = "employees.csv"

def create_sample_csv():
    rows = [["name", "department", "salary"],
            ["Alice", "Engineering", "90000"],
            ["Bob",   "Marketing",   "45000"],
            ["Carol", "HR",          "58000"],
            ["David", "Engineering", "72000"],
            ["Eve",   "Marketing",   "38000"]]
    with open(FILE, "w", newline="") as f:
        csv.writer(f).writerows(rows)

def process_csv(filename):
    with open(filename, "r") as f:
        employees = [{"name": r["name"], "department": r["department"],
                      "salary": int(r["salary"])} for r in csv.DictReader(f)]

    high_earners = [e for e in employees if e["salary"] > 50000]
    avg_salary   = sum(e["salary"] for e in employees) / len(employees)

    print(f"Total Employees : {len(employees)}")
    print(f"Salary > 50,000 : {len(high_earners)}")
    for e in high_earners:
        print(f"  {e['name']:<10} | {e['department']:<15} | Rs.{e['salary']}")
    print(f"Average Salary  : Rs.{avg_salary:.2f}")

create_sample_csv()
process_csv(FILE)
