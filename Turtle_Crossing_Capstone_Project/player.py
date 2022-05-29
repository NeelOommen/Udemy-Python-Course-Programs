STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setpos(STARTING_POSITION)
        self.left(90)


    def move_forward(self):
        x = self.xcor()
        y = self.ycor()
        self.setpos(x, y + 10)


    def go_to_start(self):
        self.setpos(STARTING_POSITION)


    def finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False