# Exercise 11: Float Input
# Objective: Convert weight from kilograms to pounds

def kg_to_lbs():
    raw = input("Enter weight in kg: ").strip()
    try:
        kg = float(raw)
    except ValueError:
        print("Error: Please enter a valid decimal number.")
        return
    if kg <= 0:
        print("Error: Weight must be positive.")
        return
    lbs = kg * 2.20462
    print(f"{kg:.2f} kg = {lbs:.2f} lbs")

kg_to_lbs()
