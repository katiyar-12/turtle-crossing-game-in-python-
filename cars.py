from turtle import Turtle
from random import randint


class Cars :
    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        new = Turtle()
        new.penup()
        new.shape("square")
        new.color(self.random_color())
        new.shapesize(stretch_wid=1, stretch_len=2)
        new.goto(300,randint(-250,250))
        new.right(180)
        self.all_cars.append(new)

    def move_cars(self):
        for item in self.all_cars :
            item.forward(10)

    def random_color(self):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

        return (r,g,b)

