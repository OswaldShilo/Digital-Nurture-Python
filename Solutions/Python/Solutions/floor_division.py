# Exercise 7: Floor Division
# Objective: Split a total bill equally among people using //

def split_bill(total_bill, people):
    if total_bill <= 0:
        raise ValueError("Total bill must be positive")
    if people <= 0:
        raise ValueError("Number of people must be positive")
    share     = total_bill // people
    remainder = total_bill % people
    print(f"Total Bill   : Rs.{total_bill}")
    print(f"People       : {people}")
    print(f"Each Share   : Rs.{share}")
    print(f"Remainder    : Rs.{remainder}")

total_bill = 1250
people     = 4
split_bill(total_bill, people)
