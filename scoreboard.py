from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.options()

    def options(self):
        self.hideturtle()
        self.goto(0, 260)
        self.pencolor("white")
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.options()


    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.options()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)