import turtle
turtle.colormode(255)
from turtle import Turtle, Screen
import random
timmy = Turtle()
lines = 1
distance = -200
all_colors = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (142, 178, 203), (139, 82, 105), (208, 90, 69), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64), (119, 46, 39), (48, 65, 61)]
timmy.penup()
timmy.setx(-220)
timmy.sety(distance)
def draw():
    for n in range(10):
        timmy.dot(20, random.choice(all_colors))
        timmy.forward(50)

while lines != 11:
    distance += 50
    lines += 1
    draw()
    timmy.setx(-220)
    timmy.sety(distance)

screen = Screen()
screen.exitonclick()