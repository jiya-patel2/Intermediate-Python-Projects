from tkinter import *
import pandas
import random

# CONSTANTS
BLUE = "#1D1257"
SAGE_GREEN = "#4C5C2D"
OLIVE_GREEN = "#313E17"
BLACK = "#1B0C0C"
FONT_NAME ="Ariel"
BACKGROUND = "#B1DDC6"
current_card ={}
to_learn = {}

# Using Pandas convert data to list
try:
    data = pandas.read_csv(".\\capstone_flash_card\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(".\\capstone_flash_card\\data\\gujarati_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
   


# NEXT CARD
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    guj_word = current_card["Gujarati"] 
    canvas.itemconfig(card_language,text="Gujarati",fill=SAGE_GREEN)
    canvas.itemconfig(card_word,text=guj_word,fill=BLACK)
    canvas.itemconfig(canvas_image,image=front_card)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image,image=back_card)
    eng_word = current_card["English"] 
    canvas.itemconfig(card_language,text="English", fill=OLIVE_GREEN)
    canvas.itemconfig(card_word,text=eng_word, fill=BLUE)
    window.after_cancel()

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(".\\capstone_flash_card\\data\\words_to_learn.csv",index=False)
    next_card()

#UI SETUP
window = Tk()
window.title("Learning Gujarati")
window.config(padx=50,pady=50,bg=BACKGROUND)

flip_timer= window.after(3000,func=flip_card)

canvas = Canvas(width= 800, height=526 , bg=BACKGROUND , highlightthickness=0)
front_card = PhotoImage(file=".\\capstone_flash_card\\images\\card_front.png")
back_card = PhotoImage(file=".\\capstone_flash_card\\images\\card_back.png")
canvas_image = canvas.create_image(400,263,image=front_card)
canvas.grid(column=0,row=0,columnspan=2)

card_language = canvas.create_text(400,150,text="",fill=SAGE_GREEN,font=(FONT_NAME,30,"italic"))

card_word = canvas.create_text(400,300,text="",fill=BLACK,font=(FONT_NAME,53,"bold"))

wrong_img = PhotoImage(file=".\\capstone_flash_card\\images\\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

right_img = PhotoImage(file=".\\capstone_flash_card\\images\\right.png")
right_button = Button(image=right_img, highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

next_card()

# window.grid_columnconfigure(1, weight=1)
window.mainloop()