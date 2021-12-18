from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.goto(0, -230)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

    def go_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def again(self):
        self.goto(0, -230)
