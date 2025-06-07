from turtle import Turtle

class Crosser(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(0,-280)

    def move_crosser_upwards(self):
        self.forward(10)

    def go_back(self):
        self.goto(0,-280)