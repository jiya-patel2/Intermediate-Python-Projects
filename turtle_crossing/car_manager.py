from turtle import Turtle
import random 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 7
        self.new_distance = 0
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_num = random.randint(0,6)
        if random_num == 1:
            car = Turtle("square")
            car.penup()
            car.resizemode("user")
            car.shapesize(stretch_wid=1, stretch_len=2, outline=0.002)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)
            rand_y = random.randint(-230,230)
            car.goto(350,rand_y)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT
        
        

