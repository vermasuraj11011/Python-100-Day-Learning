import random

rock_paper_scissors = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

users_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
print(rock_paper_scissors[users_option])

computer_option = random.randint(0, 2)
print(f"Computer choose: \n {rock_paper_scissors[computer_option]}")

if users_option == 0 and computer_option == 2 or users_option == 1 and computer_option == 0 or users_option == 2 and computer_option == 1:
    print("You win")
elif users_option == 0 and computer_option == 1 or users_option == 1 and computer_option == 2 or users_option == 2 and computer_option == 0:
    print("You lose")
else:
    print("Game draw")

