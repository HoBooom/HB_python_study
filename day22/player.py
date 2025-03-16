from turtle import Turtle

class Player(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x,y)
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        if self.ycor() < 330:
            self.setheading(90)
            self.forward(20)

    def move_down(self):
        if self.ycor() > -330:
            self.setheading(270)
            self.forward(20)