import csv
import pandas

# with open('weather_data.csv') as whether_data:
#     data = csv.reader(whether_data)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)

data = pandas.read_csv('weather_data.csv')

# print(type(data)) # <class 'pandas.core.frame.DataFrame'>

# print(type(data['temp'])) # <class 'pandas.core.series.Series'>

# convert to dictionary
# print(data.to_dict())

# to list
# print(data['temp'].to_list())

# print(data.temp)

# get row data
# row_data = data.temp[2]
# print(row_data)

# print(data[data.temp == 15])

# row with max temp
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
condition = monday.condition
print(condition)
