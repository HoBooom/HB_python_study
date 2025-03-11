from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

class Race:
    def __init__(self):
        self.red_turtle = Turtle("turtle")
        self.orange_turtle = Turtle("turtle")
        self.yellow_turtle = Turtle("turtle")
        self.green_turtle = Turtle("turtle")
        self.blue_turtle = Turtle("turtle")
        self.purple_turtle = Turtle("turtle")
        self.turtles = [self.red_turtle, self.orange_turtle, self.yellow_turtle, self.green_turtle, self.blue_turtle, self.purple_turtle]
        self.my_turtle = None
        self.winner = None

    def set_turtle_color(self):
        self.red_turtle.color('red')
        self.orange_turtle.color('orange')
        self.yellow_turtle.color('yellow')
        self.green_turtle.color('green')
        self.blue_turtle.color('blue')
        self.purple_turtle.color('purple')

    def set_position(self):
        x_position = -240
        y_position = -100
        for turtle in self.turtles:
            turtle.penup()
            turtle.goto(x_position, y_position)
            y_position += 40


    def set_my_turtle(self):
        my_color = screen.textinput("Race", "What color of turtle do u bet?")
        self.my_turtle = my_color

    def start_race(self):
        while True:
            is_end = False
            for turtle in self.turtles:
                turtle.forward(random.randint(1, 10))
                cnt_x,cnt_y = turtle.pos()
                if cnt_x >= 210:
                    is_end = True
                    self.winner = turtle.pencolor()
                    break
            if is_end:
                break
        if self.my_turtle == self.winner:
            print("u win the game")
        else:
            print("u lose the game")
            print(f"the winner is {self.winner}")




race = Race()
race.set_my_turtle()
race.set_turtle_color()
race.set_position()
race.start_race()





screen.exitonclick()