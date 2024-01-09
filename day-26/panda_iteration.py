import pandas

student_mark_dic = {
    'student': ['abhishek', 'ram', 'shyam', 'surj', 'kiran'],
    'score': [60, 19, 13, 72, 84]
}

data = pandas.DataFrame(student_mark_dic)

# for (key,value) in data.items():
#     print(value)

for (index, row) in data.iterrows():
    print(row)