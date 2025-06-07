# creating a turtle crossing game

from time import sleep
from turtle import Screen

from PIL.ImageChops import screen

from turtle_object import Crosser
from cars import Cars
from score_card import ScoreCard

# creating screen
myScreen = Screen()
myScreen.tracer(0)

# creating objects
myTurtle = Crosser()
cars = Cars()
score_board = ScoreCard()





myScreen.title("Turtle Crossing Game")
myScreen.setup(width=600, height=600)
myScreen.colormode(255)
myScreen.listen()

# function to move turtle upward
myScreen.onkey(fun=myTurtle.move_crosser_upwards,key="Up")

SLEEPING_TIME = 0.30
GAME_IS_ON = True
COUNT = 6

while GAME_IS_ON :

    # detecting whether all the levels finished
    if SLEEPING_TIME < 0 :
        GAME_IS_ON = False

    COUNT -= 1
    sleep(SLEEPING_TIME)
    myScreen.update()
    if COUNT == 1 :
        cars.generate_car()
        COUNT = 6
    cars.move_cars()

    # increment level when reach at top
    if myTurtle.ycor()  > 270 :
        score_board.increment_level()
        myTurtle.go_back()
        SLEEPING_TIME -= 0.03

    # detect collision with car
    for car in cars.all_cars :
        if myTurtle.distance(car) < 30:
            GAME_IS_ON = False
            score_board.game_over()


myScreen.exitonclick()