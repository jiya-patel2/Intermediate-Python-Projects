from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x_cor = x
        self.y_cor = y
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.color("#08F7FE")
        self.penup()
        self.goto(self.x_cor,self.y_cor)

    def go_up(self):
        if self.ycor() <= 250:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= -250:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
