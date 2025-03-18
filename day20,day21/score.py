from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align="center", font=("Courier", 24, "normal"))
        self.high_score = 0
        self.read_high_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def read_high_score(self):
        with open("data.txt", "r") as file:
            points = file.readlines()
            if len(points) > 0:
                self.high_score = int(points[-1])
            else:
                self.high_score = 0

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f'\n{self.high_score}')
        self.score = 0
        self.update_score()


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))