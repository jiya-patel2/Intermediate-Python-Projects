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
        with open("snake_Game\high_score.txt") as f:
            content = f.read()
            if content:
                self.high_score = int(content)
            else:
                self.high_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"[Score : {self.score}  High Score : {self.high_score}]", move=False, align=ALIGNMENT, font= FONT)

    def new_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if int(self.high_score) < self.score:
            self.high_score = self.score
            with open("snake_Game\high_score.txt", mode = "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"[Game Over]", move=False, align=ALIGNMENT, font= FONT)

    