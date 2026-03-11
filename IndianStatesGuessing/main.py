import turtle
import pandas 
screen = turtle.Screen()
screen.setup(width=600, height=708)
screen.title("Indian States Guessing Game")
image = "IndianStatesGuessing\\political-map.gif"
screen.addshape(image)
turtle.shape(image)
correct_guess = 0 
guessed_state = []


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guessed_state) < 37:
    data = pandas.read_csv("IndianStatesGuessing\\india_states_centered.csv")
    all_states = data.State.to_list()

    answer_state = screen.textinput(title=f"{correct_guess}/37 States Correct" , prompt="State Name :"  )
    if answer_state == "Exit":
        missing_state = [states for states in all_states if states not in guessed_state]

        data = pandas.DataFrame(missing_state)
        data.to_csv("IndianStatesGuessing\\states_to_learn.csv")
        break

    if answer_state in all_states:
        state_name = turtle.Turtle()
        state_name.color("#333333")
        state_name.penup()
        state_name.hideturtle()
        correct_guess += 1
        guessed_state.append(answer_state)
        state_data = data[data["State"] ==  answer_state]
        state_name.goto(state_data.x.item(), state_data.y.item())
        state_name.write(f"{answer_state}", align="center", font=("Arial", 10, "bold"))
  
