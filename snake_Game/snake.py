from turtle import Turtle

X_POSITION = [0,-20,-40]
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

    def create_snake(self):
        for part in X_POSITION:
            self.add_part((part,0))
            
    def add_part(self, part):
        snake_body = Turtle(shape = "square")
        snake_body.color("#D93770")
        snake_body.penup()
        snake_body.goto(part)
        self.snake.append(snake_body)

    def reset(self):
        for snake_body in self.snake:
            snake_body.goto(2000,2000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_part(self.snake[-1].position())

    def move(self):
        for part in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[part-1].xcor()
            new_y = self.snake[part-1].ycor()
            self.snake[part].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)   

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)