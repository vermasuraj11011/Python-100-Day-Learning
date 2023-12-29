from art import logo

def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def divide(first, second):
    return first / second


def multiply(first, second):
    return first * second


operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}


def calculator():
    print(logo)
    num1 = float(input("Enter the first number "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        sign = input('Select the operation from above \n')
        num2 = float(input("Enter the second number "))
        res = operations[sign](num1, num2)
        print(f'{num1} {sign} {num2} = {res}')
        if input(f"Type 'y' to continue using {res} for another operation type 'n' for new start") == 'y':
            num1 = res
        else:
            should_continue = False
            calculator()


calculator()
