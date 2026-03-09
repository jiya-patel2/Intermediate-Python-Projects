from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width =600,height = 600)
screen.title("Play with Python")
screen.bgcolor("#132440")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left,"Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food 
    if snake.head.distance(food) < 13 :
        food.refresh()
        snake.extend()
        score.new_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        score.reset()
        snake.reset()

    # Detect collision with tail
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10 :
            # is_game_on = False
            score.reset()
            snake.reset()
            

screen.exitonclick()