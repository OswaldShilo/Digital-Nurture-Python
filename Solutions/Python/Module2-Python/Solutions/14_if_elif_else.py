# Exercise 14: If-Elif-Else
# Objective: Assign grade A/B/C based on score

def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score}  ->  Grade: {grade}")

score = 88
assign_grade(score)
