from data import question_data
from question_model import Question
from quiz_brain import Quiz
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_obj = Question(question['question'], question['correct_answer'])
    question_bank.append(question_obj)

quiz = Quiz(question_bank)

game = QuizInterface(quiz)

print(f"Your final score is {quiz.score}")
