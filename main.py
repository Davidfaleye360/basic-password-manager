from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += ([choice(symbols) for _ in range(randint(2, 4))])
    password_list += ([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    site = website_entry.get()
    mail = user_entry.get()
    password = password_entry.get()
    if len(password) == 0 or len(site) == 0 or len(mail) == 0:
        messagebox.showerror(title='Check Fields', message='You have left some fields empty')
    else:
        is_okay = messagebox.askokcancel(title=site, message=f'These are the details entered:\nEmail : {mail}\nPassword : {password}\nIs it okay to save' )
        if is_okay:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            with open('data.txt', 'a') as all_data:
                all_data.write(f'{site} | {mail} | {password}'+'\n')


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title('Password Manager')
windows.config(pady=50,padx=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, padx=20, pady=20)

# labels
web_label = Label(text='website:', font=('Arial', 15))
web_label.grid(row=1, column=0)

user_label = Label(text='Email/Username:', font=('Arial', 15))
user_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=('Arial', 15))
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=58)
website_entry.focus()
website_entry.grid(column=1, columnspan=2, row=1)

user_entry = Entry(width=58)
user_entry.grid(column=1, columnspan=2, row=2)
user_entry.insert(0, 'mail@gmail.com')

password_entry = Entry(width=39)
password_entry.grid(column=1, row=3)

# buttons
password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=49, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)


windows.mainloop()
