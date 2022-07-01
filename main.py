from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
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

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    generated_password = "".join(password_list)
    Password_text.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = Website_text.get()
    email = Email_text.get()
    password = Password_text.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # reading the data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating the data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving the updated data
                json.dump(data, data_file, indent=4)

        finally:
            Website_text.delete(0, END)
            Password_text.delete(0, END)
            Email_text.delete(0, END)


def search():
    with open("data.json", "r") as data_file:
        # reading the data
        data = json.load(data_file)
        website = Website_text.get()
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f'Email: {data[website]["email"]}\n Password: '
                                                            f'{data[website]["password"]}')
        else:
            messagebox.showinfo(title="Oops", message="There is no result")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=250, height=350)
window.config(padx=20, bg="white")

canvas = Canvas(width=220, height=220, bg="white", highlightthickness=0)

logo_img = PhotoImage(file="logo.png")

canvas.create_image(109, 109, image=logo_img)
canvas.grid(column=1, )

Website_text = Entry(width=32, )
Website_label = Label(text="Website: ", font=("Times New Roman", 10), bg="white")
Website_label.grid(column=0, row=1)
Website_text.grid(column=1, row=1,)
Website_text.focus()

Search_button = Button(text="Search", height=1, width=15, bg="teal", command=search)
Search_button.grid(column=2, row=1, )

Email_text = Entry(width=50, )
Email_label = Label(text="Email/Username:  ", font=("Times New Roman", 10), bg="white")
Email_label.grid(column=0, row=2, )
Email_text.grid(column=1, row=2, columnspan=2)
Email_text.insert(0, "mohammedalaa40123@gmail.com")

Password_text = Entry(width=32, )
Password_label = Label(text="Password ", font=("Times New Roman", 10), bg="white")
Password_label.grid(column=0, row=3, )
Password_text.grid(column=1, row=3, )

Generate_button = Button(text="Generate Password", bg="white", height=1, command=generate_password)
Generate_button.grid(column=2, row=3, )

add_button = Button(text="add", width=40, bg="white", height=1, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
