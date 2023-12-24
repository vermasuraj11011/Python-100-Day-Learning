from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        if new_position >= 26:
            new_position = new_position % 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is \n{cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ''
    for char in cipher_text:
        position = alphabet.index(char)
        original_position = position - shift_amount
        if original_position < 0:
            original_position = 26 + original_position
        original_letter = alphabet[original_position]
        plain_text += original_letter
    print(f"The decoded text is \n{plain_text}")


def caesar(dire, cip_text, cip_shift):
    cipher_text = ''
    for char in cip_text:
        pos = alphabet.index(char)
        if dire == 'encode':
            pos += cip_shift
            if pos >= 26:
                pos %= 26
        else:
            pos -= cip_shift
            if pos < 0:
                pos += 26
        cipher_text += alphabet[pos]
    print(f"The {dire} text is \n{cipher_text}")


while True:
    again = input('Type "y/Y" to continue "n/N" to exit \n').lower()
    if again == 'n':
        break
    elif again == 'y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26
        caesar(direction, text, shift)
    else:
        print('Please enter valid inputs \n')

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("please type 'encode' to encrypt, type 'decode' to decrypt:\n")
