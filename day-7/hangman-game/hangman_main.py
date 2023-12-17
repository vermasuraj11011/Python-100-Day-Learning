import random
from hangman_word import word_list
from hangman_art import logo
from hangman_art import stages

word = random.choice(word_list)
word_len = len(word)
isGameOver = False

print(logo)
print(word)
lives = 6

display = []
for _ in range(word_len):
    display += "_"

while not isGameOver:
    guess = input("Guess a letter: ").lower()

    for i in range(word_len):
        if word[i] == guess:
            display[i] = guess

    if guess not in word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

    print(f"{' '.join(display)}")
    print(stages[lives])

    if lives == 0:
        print("Game Over")
        isGameOver = True
    elif '_' not in display:
        print("You Won")
        isGameOver = True

    print(display)
#
