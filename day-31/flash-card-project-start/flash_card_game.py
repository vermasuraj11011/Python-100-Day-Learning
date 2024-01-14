import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
list_data_dict = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    list_data_dict = original_data.to_dict(orient='records')
else:
    list_data_dict = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list_data_dict)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    list_data_dict.remove(current_card)
    print(len(list_data_dict))
    data = pandas.DataFrame(list_data_dict)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
know_btn = Button(image=right_image, highlightthickness=0, command=is_known)
know_btn.grid(row=1, column=1)

next_card()

window.mainloop()
