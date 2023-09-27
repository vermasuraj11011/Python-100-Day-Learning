import math

print("Welcome to BMI calculator")

height = float(input("Enter your height in 'meter': "))
weight = int(input("Enter your weight in 'Kg': "))

bmi_value = int(math.floor(weight / (height ** 2)))

print(f"Your BMI score is {bmi_value}")
