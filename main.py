from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


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
    site = website_entry.get().title()
    mail = user_entry.get()
    password = password_entry.get()
    new_data = {
        site: {
            'email': mail,
            'password': password
        }
    }
    if len(password) == 0 or len(site) == 0 or len(mail) == 0:
        messagebox.showerror(title='Check Fields', message='You have left some fields empty')
    else:
        update_or_not = True
        try:
            with open('data.json', 'r') as all_data:
                data = json.load(all_data)
        except FileNotFoundError:
            with open('data.json', 'w') as all_data:
                json.dump(new_data, all_data, indent=4)
        else:
            if site in data:
                update_or_not = messagebox.askokcancel(title='Data already exists', message='You have already saved a password and username for that site.\nDo you want to update it?\nTo check the previously  saved info, click search.')
            if update_or_not:
                data.update(new_data)
                with open('data.json', 'w') as all_data:
                    json.dump(data, all_data, indent=4)
        finally:
            if update_or_not:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# --------------------------- Search ---------------------------------- #
def find_password():
    try:
        with open('data.json', 'r') as all_data:
            data = json.load(all_data)
    except FileNotFoundError:
        messagebox.showerror(title='File does not exist', message='No data have been saved yet')
    else:
        web = website_entry.get().title()
        if web not in data:
            messagebox.showerror(title='Data does not exist', message=f'No details for {web} exists.')
        else:
            user_name = data[web]['email']
            password = data[web]['password']
            pyperclip.copy(password)
            messagebox.showinfo(title='website data', message=f'User Name: {user_name}\nPassword: {password}\nThe password has been copied to your clipboard. You can paste it where needed.')


# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title('Password Manager')
windows.config(pady=50, padx=50)


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
website_entry = Entry(width=39)
website_entry.focus()
website_entry.grid(column=1, row=1)

user_entry = Entry(width=58)
user_entry.grid(column=1, columnspan=2, row=2)
user_entry.insert(0, 'mail@gmail.com')

password_entry = Entry(width=39)
password_entry.grid(column=1, row=3)

# buttons
search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(row=1, column=2)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=49, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
