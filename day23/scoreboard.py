from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.stage = 1
        self.update()

    def update(self):
        self.write(f"Stage: {self.stage}", align="center", font=FONT)

    def next_stage(self):
        self.stage += 1
        self.clear()
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
