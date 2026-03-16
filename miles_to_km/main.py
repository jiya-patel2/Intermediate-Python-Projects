from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width= 250, height= 200)

input = Entry(width= 15)
input.insert(END, string= 0)
input.grid(row=0,column=1)

miles = Label(text = "Miles")
miles["font"] = "Arial,11,Bold"
miles.grid(row=0, column=2)



convert = Label(text = f" is equal to")
convert.grid(row=2, column=1)
convert["font"] = "Arial,11"

km = Label(text = f"0 km")
km.grid(row=2, column=2)
km["font"] = "Arial,11"

def button_clicked():
    print("Button was clicked")
    x_miles = int(input.get())
    x_km = x_miles * 1.609
    km["text"]= f"{x_km}km"

calculate = Button(text = "Calculate", command= button_clicked)
calculate.grid(row=1,column=1)


window.mainloop()
