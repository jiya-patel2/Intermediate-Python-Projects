from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#3B9797")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"[Score : {self.score}]", move=False, align=ALIGNMENT, font= FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"[Game Over]", move=False, align=ALIGNMENT, font= FONT)