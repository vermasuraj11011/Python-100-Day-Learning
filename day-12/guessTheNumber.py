from art import logo
import random


def guess_the_number():
    print('Welcome to number guessing game')
    print('I am thinking of number between 1 to 100')
    num = random.randint(1, 100)

    level = input('Choose difficulty level "hard" or "easy" ').lower()

    if level == 'hard':
        print('You have 5 attempts to guess the number')
        attempts = 5
    else:
        print('You have 10 attempts to guess the number')
        attempts = 10

    user_guess = 0
    while True:
        attempts -= 1
        if attempts <= 0:
            print(f"You lose the was {num}")
            break
        user_guess = int(input('Make a guess '))
        if user_guess > num:
            print('Too High')
        elif user_guess < num:
            print('Too Low')
        else:
            print(f'You got it, the answer was {user_guess}')
            break

        print('Guess Again')
        print(f'You have {attempts} remaining to guess the number')


print(logo)
while input('Enter "y" to play game ') == 'y':
    guess_the_number()
