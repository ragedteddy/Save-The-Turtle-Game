import turtle
from turtle import Screen
from car import Car
from random import randint
from player import Player
from level import Level

screen = Screen()
screen.tracer()
screen.listen()
cars = []
speed = 15
player = Player()
current_level = Level()

turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")

for i in range(20):
    new_car = Car()
    cars.append(new_car)


def reload():
    player.again()
    for i in range(20):
        cars[i].goto(randint(400, 1500), cars[i].ycor())


game_is_on = True

while game_is_on:
    screen.update()

    if player.ycor() > 200:
        current_level.update()
        reload()

    for i in range(20):
        if player.distance(cars[i]) < 30:
            current_level.gameover()
            game_is_on = False
            break
        cars[i].backward(current_level.cur_level * 10 + 10)
        if cars[i].xcor() < -410:
            cars[i].goto(randint(400, 1500), cars[i].ycor())

screen.exitonclick()
