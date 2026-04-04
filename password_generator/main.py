from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

# CONSTANTS
LIGHT_PINK = "#F9B2D7"
CREAM ="#F8F4EC"
PINK = "#D63484"
PURPLE = "#402B3A"
FONT =("Times New Roman",15,"bold")

# ADD DETAILS
def add_detail():
    website = input_website.get()
    email = input_username.get()
    password = input_pass.get()
    if website == "" or password == "":
        messagebox.showerror(title="Oops",message="Please don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are details\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok :
            with open (".\\password_generator\\data.txt","a+") as file:
                file.write(f"{website} : {email} | {password}\n")
            input_website.delete(0,END)
            input_pass.delete(0,END)

# GENERATE PASSWORD
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]
    password = password_letters + password_numbers + password_symbol
    shuffle(password)

    password_str= "".join(password)
    input_pass.insert(0,password_str)
    pyperclip.copy(password_str)

# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=30,bg=PURPLE)

canvas = Canvas(width=200, height=200,bg= PURPLE, highlightthickness=0)
lock_img = PhotoImage(file = "password_generator\\lock.png")
canvas.create_image(100,100, image = lock_img)
canvas.grid(column=1,row=0)


# LABELS
website_name = Label(text= "Website:", fg =PINK, bg=PURPLE, font = FONT,pady=5)
website_name.grid(column=0, row=2)

username = Label(text= "Email/Username:", fg =PINK, bg=PURPLE, font = FONT,pady=5)
username.grid(column=0, row=3)

password = Label(text= "Password:", fg =PINK, bg=PURPLE, font = FONT,pady=5)
password.grid(column=0, row=4)


# ENTERIES
input_website = Entry(width=35,bg= PURPLE,fg=CREAM)
input_website.grid(row=2,column=1,columnspan=2)

input_username = Entry(width=35,bg= PURPLE,fg=CREAM)
input_username.insert(0,"xyz@gmail.com")
input_username.grid(row=3,column=1,columnspan=2)

input_pass = Entry(width=21,bg= PURPLE,fg=CREAM)
input_pass.grid(row=4,column=1)

# BUTTONS
gen_pass = Button(text="Generate Password",bg=PURPLE,fg=LIGHT_PINK,command=generate_pass,pady=5)
gen_pass.grid(column=2,row=4)

add_details = Button(text="Add",bg=PURPLE,fg=LIGHT_PINK,width=36,command= add_detail,pady=10)
add_details.grid(column=2,row=5,columnspan=1)

window.grid_columnconfigure(1, weight=1)
window.mainloop()