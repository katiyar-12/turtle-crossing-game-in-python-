from turtle import Turtle

FONT =('Arial' ,15,'normal')
ALIGNMENT = 'left'

class ScoreCard(Turtle) :
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_no = 1
        self.write_score()

    def write_score(self):
        self.goto(-250, 250)
        self.write(f"Level {self.level_no}", False, align=ALIGNMENT, font=FONT)

    def increment_level(self):
        self.clear()
        self.write_score()
        self.level_no += 1

    def game_over(self):
        self.clear()
        self.write_score()
        self.goto(0,0)
        self.write("GAME OVER" ,move=False,align="center",font=FONT)