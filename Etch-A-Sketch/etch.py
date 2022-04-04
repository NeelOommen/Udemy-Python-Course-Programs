from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(5)


def move_backward():
    t.back(5)


def turn_right():
    t.right(5)


def turn_left():
    t.left(5)


def turtle_clear():
    t.reset()


screen.listen()

#controls
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=turtle_clear)


screen.exitonclick()