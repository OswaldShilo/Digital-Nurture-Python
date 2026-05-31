# Exercise 12: Simple If
# Objective: Check pass/fail based on marks

def check_pass_fail(marks):
    if not isinstance(marks, (int, float)):
        raise TypeError("Marks must be a number")
    if not (0 <= marks <= 100):
        raise ValueError("Marks must be between 0 and 100")
    if marks >= 50:
        print(f"Marks: {marks} -> Pass")
    else:
        print(f"Marks: {marks} -> Fail")

marks = 75
check_pass_fail(marks)
