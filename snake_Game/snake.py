from turtle import Turtle,Screen

X_POSITION = [-40, -20, 0]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self,):
        for part in X_POSITION:
            snake_body = Turtle(shape = "square")
            snake_body.color("#FDB5CE")
            snake_body.penup()
            snake_body.goto(part,0)
            self.snake.append(snake_body)

    def move(self):
        for part in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[part-1].xcor()
            new_y = self.snake[part-1].ycor()
            self.snake[part].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)   

    def up(self):
        if self.head.heading != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading != RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT :
            self.head.setheading(RIGHT)