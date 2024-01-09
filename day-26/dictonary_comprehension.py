import random

names = ['abhishek', 'ram', 'shyam', 'suraj', 'kiran']

student_score = {name: random.randint(1, 100) for name in names}
print(student_score)

pass_students = {key: value for (key, value) in student_score.items() if value > 33}
print(pass_students)

string_eg = 'My name is suraj verma'
word_dic = {word: len(word) for word in string_eg.split(' ')}
print(word_dic)