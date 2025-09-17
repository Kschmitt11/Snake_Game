from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.options()

    def options(self):
        self.hideturtle()
        self.goto(0, 260)
        self.pencolor("white")
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.options()
