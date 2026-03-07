FONT = ("Courier", 24, "normal")
ALIGNMENT = "right"
LEVELS = 10
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#EAEAEA")
        self.penup()
        self.hideturtle()

        self.level_num = 1
        self.goto(-50,265)
        self.write(f"[LEVEL : {self.level_num}]", align=ALIGNMENT, font=FONT)

        

    def update_level(self):
        if self.level_num < LEVELS:
            self.level_num += 1
            self.clear()
            self.write(f"[LEVEL : {self.level_num}]", align=ALIGNMENT, font=FONT)
        elif self.level_num == LEVELS:
            self. goto(0,0)
            self.clear()
            self.color("#4CAF50")
            self.write(f"YOU WON", move=False, align="center", font= FONT)

    def game_over(self):
        self. goto(0,0)
        self.clear()
        self.color("#E63946")
        self.write(f"YOU LOST", move=False, align="center", font= FONT)

