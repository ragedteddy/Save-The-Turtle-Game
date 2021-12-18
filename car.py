import turtle
from turtle import Turtle
from random import randint

turtle.colormode(255)


class Car(Turtle):

    def __init__(self):
        super(Car, self).__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color(randint(0, 255),
                   randint(0, 255),
                   randint(0, 255))
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.goto(randint(400, 1500), randint(-200, 200))
        self.showturtle()
