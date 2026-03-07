from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#2ECC71")
        self.shape("turtle")
        self.penup()
        self.y_move = 10
        self.left(90)
        self.reset_postion()

    def forward(self):
        new_y = self.ycor() + self.y_move 
        self.goto(self.xcor(), new_y)

    def reset_postion(self):
        self.goto(STARTING_POSITION)
        self.penup()
        
    