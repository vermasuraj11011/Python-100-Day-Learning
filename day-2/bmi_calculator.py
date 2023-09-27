import math

print("Welcome to BMI calculator")

height = float(input("Enter your height in 'meter': "))
weight = int(input("Enter your weight in 'Kg': "))

bmi_value = int(math.floor(weight / (height ** 2)))

print(f"Your BMI score is {bmi_value}")

if bmi_value < 18.5:
    print("You are 'Under' weight")
elif 18.5 < bmi_value < 25:
    print("You are 'Normal' weight")
elif 25 < bmi_value < 30:
    print("You are 'Over' weight")
elif 30 < bmi_value < 35:
    print("You are 'Obese' weight")
else:
    print("You are 'Clinically Obese'")
