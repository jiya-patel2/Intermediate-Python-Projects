from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width =800,height = 600)
screen.title("Play with Python")
screen.bgcolor("#0F1020")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, 'W')
screen.onkey(l_paddle.go_down, 'S' )

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall w.r.t it's height i.e 600
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with Paddle
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 330) or (ball.distance(l_paddle) < 60 and ball.xcor() < -330) :
        ball.bounce_x()

    #Detect collision with wall w.r.t it's width i.e 800 (r_paddle miss)
    if ball.xcor() > 380 :
        ball.reset_postion()
        score.l_point()

    #Detect collision with wall w.r.t it's width i.e 800 (l_paddle miss)
    if ball.xcor() < -380 :
        ball.reset_postion()
        score.r_point()

screen.exitonclick()
