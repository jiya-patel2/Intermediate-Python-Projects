from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#FFFFFF")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-150,250)
        self.write(f"[Player 1 : {self.l_score}] ", move=False, align=ALIGNMENT, font= FONT)
        self.goto(150,250)
        self.write(f"[Player 2 : {self.r_score}] ", move=False, align=ALIGNMENT, font= FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()   

    def game_over(self):
        self.goto(0,0)
        self.write(f"[Game Over]", move=False, align=ALIGNMENT, font= FONT)
        