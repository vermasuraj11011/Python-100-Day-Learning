numbers = [1, 2, 3, 4, 5]
add_two = [n + 2 for n in numbers]
print(add_two)

name = 'suraj'
letters = [letter for letter in name]
print(letters)

multiple_two = [n * 2 for n in range(1, 5)]
print(multiple_two)

names = ['abhishek', 'ram', 'shyam', 'suraj', 'kiran']
names_with_s = [name_s for name_s in names if name_s.startswith('s')]
print(names_with_s)