std_score = input("Enter the score of student:\n").split(" ")

maxScore = 0
for score in std_score:
    if maxScore < int(score):
        maxScore = int(score)

print(f"Max score is {maxScore}")
