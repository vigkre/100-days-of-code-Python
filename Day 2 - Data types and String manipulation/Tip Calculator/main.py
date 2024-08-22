print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $ "))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
members = int(input("How many people to split the bill? "))
bill_per_person = ((tip_amount / 100) * total_bill + total_bill) / members
print(f"Each person should pay: $ {round(bill_per_person, 2)}")
