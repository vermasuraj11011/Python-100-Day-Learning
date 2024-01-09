import pandas

words_data = pandas.read_csv('nato_phonetic_alphabet.csv')

key_word_dict = {row.letter: row.code for (index, row) in words_data.iterrows()}

user_input = input('Enter the word which you want to convert to phonetic: ').upper()

user_resp = [key_word_dict[letter] for letter in user_input]

print(user_resp)
