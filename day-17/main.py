from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []

for question in question_data:
    question_obj = Question(question['text'], question['answer'])
    question_bank.append(question_obj)

quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"Your final score is {quiz.score}")

# print(question_bank)
