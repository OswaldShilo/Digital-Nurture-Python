# Exercise 36: Set Intersection
# Objective: Find common skills between two sets using &

def common_skills(skills_a, skills_b):
    if not isinstance(skills_a, set) or not isinstance(skills_b, set):
        raise TypeError("Inputs must be sets")
    common = skills_a & skills_b
    print(f"Skills A      : {skills_a}")
    print(f"Skills B      : {skills_b}")
    print(f"Common Skills : {common}")
    return common

dev_skills     = {"Python", "SQL", "Git", "Docker", "Linux"}
analyst_skills = {"Python", "SQL", "Excel", "Tableau", "Power BI"}
common_skills(dev_skills, analyst_skills)
