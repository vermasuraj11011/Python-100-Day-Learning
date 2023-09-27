print("Welcome to the tip calculator")

bill_amount = float(input("What was the total bill? "))
tip_amount = int(input("What percentage tip would you want to give? (10, 12 or 15) "))
number_of_people = int(input("How many people to split the bill? "))

total_amount = bill_amount * (1 + tip_amount / 100)
amount_per_person = total_amount / number_of_people
round_to_two_deci = round(amount_per_person, 2)

print(f"Each person should pay: " + str(round_to_two_deci))
