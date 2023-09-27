print("Welcome to Leap year finder app (:")

year = int(input("Enter the year to check: "))

notLeapYear = f"{year} is not a leap year"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(notLeapYear)
    else:
        print(f"{year} is a leap year")
else:
    print(notLeapYear)
