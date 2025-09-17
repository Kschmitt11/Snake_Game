from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.options()

    def options(self):
        self.hideturtle()
        self.goto(0, 260)
        self.pencolor("white")
        self.write(f"Score = {self.score}", align="center", font=("Arial", 14, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.options()
