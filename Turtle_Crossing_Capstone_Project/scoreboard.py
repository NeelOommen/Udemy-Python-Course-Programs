FONT = ("Courier", 12, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()

    def write_scoreboard(self, level):
        self.clear()
        self.pu()
        self.setpos(-290, 280)
        self.pd()
        self.write(f"Level: {level}", False, align = "left", font = FONT)


    def game_over(self):
        self.pu()
        self.setpos(-50,0)
        self.pd()
        self.write("Game Over.", False, align = "left", font = FONT)