from tkinter import *
import math
# CONSTANTS
RED = "#FF0000"
CREAM = "#FFE8C5"
PEACH = "#FFA27F"
GREEN = "#778F52"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# TIMER RESET
def reset_timer():
    global timer 
    timer = window.after_cancel(timer) 
    canvas.itemconfig(timer_text,text="00:00")
    checkmark.config(text="")
    title_label.config(text="Timer")
    global reps 
    reps = 0

# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

        #If it's the 8th rep:
    if reps %8 == 0:
        count_down(long_break_sec)
        title_label.config(text= "Break", fg =RED)
    
    
    #If it's 2nd/4th/6th rep:
    elif reps %2 == 0:
        count_down(short_break_sec)
        title_label.config(text= "Timer", fg =PEACH)

    #If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title_label.config(text= "Timer", fg =GREEN)
        


# COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        tick= ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            tick += "✓"
        checkmark.config(text= tick)


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=90, pady= 50, bg= CREAM )

title_label = Label(text= "Timer", fg =GREEN, bg=CREAM, font = (FONT_NAME,40,"bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224,bg= CREAM, highlightthickness=0)
tomato_img = PhotoImage(file = "pomodoro_tomato\\tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text= canvas.create_text(100,130, text= "00:00", fill= CREAM, font= (FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",background=CREAM, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",background=CREAM,command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN,bg=CREAM)
checkmark.grid(column=1, row=3)
window.mainloop()