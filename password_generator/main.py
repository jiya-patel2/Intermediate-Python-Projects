from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# CONSTANTS
LIGHT_PINK = "#F9B2D7"
CREAM ="#F8F4EC"
PINK = "#D63484"
PURPLE = "#402B3A"
FONT =("Times New Roman",15,"bold")

# ERASE DATA FROM WINDOW
def erase_data():
    input_website.delete(0,END)
    input_pass.delete(0,END)

# ADD DETAILS
def add_detail():
    website = input_website.get()
    email = input_username.get()
    password = input_pass.get()
    new_data = {
            website:{
                    "email" : email,
                    "password" : password,
                    }
                }
    
    if website == "" or password == "":
        messagebox.showerror(title="Oops",message="Please don't leave fields empty")
    else:
        try :
            with open (".\\password_generator\\data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open (".\\password_generator\\data.json","w") as file:
                json.dump(data, file,indent=4)
        else :
            data.update(new_data)

            with open (".\\password_generator\\data.json","w") as file:
                json.dump(data, file,indent=4)
        finally: 
            erase_data()

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

# SEARCH PASSWORD
def find_pass():
    website = input_website.get()
    try :
        with open (".\\password_generator\\data.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data file found")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error",message="No Data file found")
    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"email: {data[website][0]}/nPassword: {data[website][1]}")
        else:
            messagebox.showerror(title="Error",message="No details for website exist")
    

# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=30,bg=PURPLE)

canvas = Canvas(width=200, height=200,bg= PURPLE, highlightthickness=0)
lock_img = PhotoImage(file = "password_generator\\lock.png")
canvas.create_image(100,100, image = lock_img)
canvas.grid(column=1,row=0)


# LABELS
website_name = Label(text= "Website:", fg =PINK, bg=PURPLE, font = FONT)
website_name.grid(column=0, row=2, pady=5, sticky="E")

username = Label(text= "Email/Username:", fg =PINK, bg=PURPLE, font = FONT,pady=5)
username.grid(column=0, row=3,sticky="E")

password = Label(text= "Password:", fg =PINK, bg=PURPLE, font = FONT,pady=5)
password.grid(column=0, row=4,sticky="E")


# ENTERIES
input_website = Entry(width=30,bg= PURPLE,fg=CREAM)
input_website.grid(row=2,column=1,sticky="W")

input_username = Entry(width=35,bg= PURPLE,fg=CREAM)
input_username.insert(0,"xyz@gmail.com")
input_username.grid(row=3,column=1,columnspan=2,sticky="W")

input_pass = Entry(width=30,bg= PURPLE,fg=CREAM)
input_pass.grid(row=4,column=1,sticky="W")

# BUTTONS
gen_pass = Button(text="Generate Password",bg=PURPLE,fg=LIGHT_PINK,command=generate_pass,pady=2,padx=8)
gen_pass.grid(column=2,row=4,sticky="W")

search_pass = Button(text="Search",bg=PURPLE,fg=LIGHT_PINK,command=find_pass,pady=2,padx=10)
search_pass.grid(column=2,row=2,sticky="W")

add_details = Button(text="Add",bg=PINK,fg=CREAM,width=20,command= add_detail,padx=8,pady=4)
add_details.grid(column=1,row=5)

window.grid_columnconfigure(1, weight=1)
window.mainloop()