from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please enter all fields")
    else:
    #is_ok = messagebox.askokcancel(title="Save Password", message=f"These are the details entered: \nEmail : {email}\nWebsite : {website}\nPassword : {password}, Is it ok to save?")
    #if is_ok:
    # saved_file.write(f"\n{website} | {email} | {password}")
        try:
            with open(f"./password.json", mode="r") as saved_file:
                data = json.load(saved_file)
        except:
            with open(f"./password.json", mode="w") as saved_file:
                json.dump(new_data, saved_file,indent=4)
        else:
            data.update(new_data)
            with open(f"./password.json", mode="w") as saved_file:
                json.dump(data, saved_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def show_password():
    website = website_entry.get()
    with open(f"./password.json", mode="r") as saved_file:
        data = json.load(saved_file)
    try:
        messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
    except:
        messagebox.showinfo(title="Error", message="Can't find email information")

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Password Manager')
window.config(padx = 20, pady = 20, bg = 'white')

canvas = Canvas(width=200, height=200, background='white', highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", background='white', fg='black')
website_label.grid(row=1, column=0)
website_entry = Entry(width=21, background='white', fg="black", highlightthickness=0)
website_entry.grid(row=1, column=1)
website_entry.focus()
website_password_search_btn = Button(text="Search", background='white', fg='black', command=show_password)
website_password_search_btn.config(width=13, highlightbackground='white')
website_password_search_btn.grid(row=1, column=2)

email_label = Label(text="Email/Username:", bg='white', fg='black')
email_label.grid(row=2, column=0)
email_entry = Entry(width=38, bg='white', fg="black", highlightthickness=0)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"abc123@google.com")

password_label = Label(text="Password:", bg='white', fg='black')
password_label.grid(row=3, column=0)
password_entry = Entry(width=21, bg='white', fg="black", highlightthickness=0,show="*")
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password", highlightbackground='white', command=generate_password)
password_button.config(width=13)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightbackground='white', command=save_password)
add_button.config(width=35)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()