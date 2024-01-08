import pandas

data_dict = {
    'name': ['suraj', 'shyam'],
    'age': [23, 35]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('new_data.csv')
