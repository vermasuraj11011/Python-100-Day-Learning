with open('data.txt') as file:
    data = file.read()
    print(data)

# opening file in write mode
with open('data.txt', 'w') as write_file:
    write_data = 'Adding new data'
    write_file.write(write_data)

# append mode
with open('data.txt', 'a') as write_file_append:
    write_data = '\nAdding new line '
    write_file_append.write(write_data)

# create new file
with open('data_1.txt', 'w') as create_if_not:
    write_data = '\ncreating new file '
    create_if_not.write(write_data)

# file = open('data.txt')
#
# print(file.read())
#
# file.close()
