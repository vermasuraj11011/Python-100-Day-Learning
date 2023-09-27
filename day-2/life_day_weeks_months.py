# Life is 90 years

age = int(input("Your current age: "))
rem_age = 90 - age
days = rem_age * 365
weeks = int(days / 7)
month = rem_age * 12

print(f"You have {days} days, {weeks} weeks and {month} months remaining :(")
