from turtle import Turtle
from turtle import Screen
import colorgram
import random

screen = Screen()


t = Turtle()
t.speed('fastest')
t.ht()
t.width(15)
screen.tracer(0)
screen.colormode(255)


colors = colorgram.extract('images\headFullOfDreamsArt.png',30)
rgbColors = []
for c in colors:
    if sum((c.rgb.r ,c.rgb.g, c.rgb.b)) > 250:
        rgbColors.append((c.rgb.r ,c.rgb.g, c.rgb.b))



turns = [0, 90, 180, 270]
for _ in range(0, 1000001):
    #clamp turtle within bounds
    if t.xcor() >= 250:
        t.setheading(180)
    elif t.xcor() <= -250:
        t.setheading(0)

    if t.ycor() >= 250:
        t.setheading(270)
    elif t.ycor() <= -250:
        t.setheading(90)

    t.pencolor(random.choice(rgbColors))
    t.forward(25)
    t.right(random.choice(turns))
    screen.update()


screen.exitonclick()