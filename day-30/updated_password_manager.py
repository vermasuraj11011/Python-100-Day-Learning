from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Entry can not be empty")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data has been saved yet ):')
    else:
        if website in data:
            password = data[website]['password']
            email = data[website]['email']
            password_entry.insert(0, password)
            email_entry.insert(0, email)
        else:
            messagebox.showinfo(title='Opps ):', message=f'Give website data not available: {website}')


# -------------------------- FIND PASSWORD ---------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_ing = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_ing)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email / Username :")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "suraj@gmail.com")
password_entry = Entry(width=45)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_password_btn = Button(text="Generate Password", width=15, command=generate_password)
generate_password_btn.grid(row=3, column=2)
add_password_btn = Button(text="Add", width=35, command=save)
add_password_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
