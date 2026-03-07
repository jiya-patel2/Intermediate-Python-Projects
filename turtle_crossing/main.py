import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("beige")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()

    for i in range(car_manager.number):
        car_manager.create_car()
        car_manager.move()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) <= 15:
            game_is_on = False
            score_board.game_over()

    #Detect if player has reached final point
    if player.ycor() >= 231:
        print("You won")
        # level ++
        car_manager.new_level()        
        player.reset_postion()
        score_board.update_level()
        
     

screen.exitonclick()