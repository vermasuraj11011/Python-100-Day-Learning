import pandas

data = pandas.read_csv('Squirrel_Data.csv')

cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

print(cinnamon_count)
print(gray_count)
print(black_count)

squirrel_count_dict = {
    'Fur Color': ['Cinnamon', 'Gray', 'Black'],
    'count': [cinnamon_count, gray_count, black_count]
}

squirrel_count_dataframe = pandas.DataFrame(squirrel_count_dict)

squirrel_count_dataframe.to_csv('squirrel_count.csv')
