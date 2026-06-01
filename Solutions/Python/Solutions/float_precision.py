def calculate_net_salary(salary, tax_rate):
    if salary <= 0:
        raise ValueError("Salary must be positive")
    if not (0 < tax_rate < 1):
        raise ValueError("Tax rate must be between 0 and 1")
    tax = salary * tax_rate
    return salary - tax

salary   = 75000.5
tax_rate = 0.18

net = calculate_net_salary(salary, tax_rate)
print(f"Gross Salary : Rs.{salary:.2f}")
print(f"Tax (18%)    : Rs.{salary * tax_rate:.2f}")
print(f"Net Salary   : Rs.{net:.2f}")