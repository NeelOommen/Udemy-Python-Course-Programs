from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','(',')','*','+']

def gen_password():
    number_of_letters = random.randint(8,10)
    number_of_numbers = random.randint(2,4)
    number_of_symbols = random.randint(2,4)

    password_list = []

    for _ in range(number_of_letters):
        password_list.append(random.choice(letters))

    for _ in range(number_of_numbers):
        password_list += random.choice(numbers)

    for _ in range(number_of_symbols):
        password_list += random.choice(symbols)

    random.shuffle(password_list)
    generated_password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)

    pyperclip.copy(generated_password)

    messagebox.showinfo(title="Password Generated", message="Generated Password copied to your clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Incomplete Information", message="Please fill in all the fields.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"Email = {email_entry.get()}\nPassword = {password_entry.get()}\nSave?")
        if is_ok:
            with open("passwords.txt", "a", encoding="utf-8") as f:
                write_line = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
                f.write(write_line)
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# get image
canvas = Canvas(width=200, height=189)
image_data = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image_data)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entry boxes
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"placeholder@email.com")

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

# Button
generate_button = Button(text="Generate Password", command=gen_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save_password, width=35)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()