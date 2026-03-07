from turtle import Turtle
import random 

COLORS = [
    "#FF4D8D",  # pink
    "#9B5DE5",  # purple
    "#00BBF9",  # blue
    "#00F5D4",  # cyan
    "#FEE440",  # yellow
    "#F15BB5"   # magenta
]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.number = 7
        self.new_distance = 0
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_num = random.randint(0,6)
        if random_num == 1:
            rand_y = random.randint(-230,230)

            # check if another car is too close
            for car in self.all_cars:
                if abs(car.ycor() - rand_y) < 20:
                    return   # don't create the car
                
            car = Turtle("square")
            car.penup()
            car.resizemode("user")
            car.shapesize(stretch_wid=1, stretch_len=2, outline=0.002)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)
            car.goto(350,rand_y)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT
        
        

