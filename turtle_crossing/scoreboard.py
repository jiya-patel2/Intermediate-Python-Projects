FONT = ("Courier", 24, "normal")
ALIGNMENT = "right"
LEVELS = 10
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#FFFFFF")
        self.penup()
        self.hideturtle()

        self.level_num = 1
        self.goto(-50,265)
        self.update_level()
        

    def update_level(self):
        self.write(f"[LEVEL : {self.level_num}] ", move=False, align=ALIGNMENT, font= FONT)
        if self.level_num < LEVELS:
            self.clear()
            self.level_num += 1
        elif self.level_num == LEVELS:
            self. goto(0,0)
            self.clear()
            self.write(f"YOU WON", move=False, align=ALIGNMENT, font= FONT)

    def game_over(self):
        self. goto(0,0)
        self.clear()
        self.write(f"YOU LOST", move=False, align=ALIGNMENT, font= FONT)

