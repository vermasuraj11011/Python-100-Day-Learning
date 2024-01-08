with open('./Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()
    for name in names:
        with open('./Input/Letters/starting_letter.txt') as letter_file:
            letter = letter_file.read()
            simple_name = name.replace('\n', '')
            with open(f'./Input/Names/invited_{simple_name}.txt', 'w') as write_letter:
                personal_invite = letter.replace('[name]', simple_name)
                write_letter.write(personal_invite)
