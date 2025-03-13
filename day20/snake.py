from turtle import Turtle,Screen
import food
import score
import time

class Snake:
    def __init__(self):
        self.snake = []
        self.screen = Screen()

    def set_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title("My Snake Game")


    def new_snake(self):
        start_x,start_y = 0,0
        for i in range(4):
            segment = Turtle(shape = "square")
            segment.color("white")
            segment.penup()
            segment.goto(start_x,start_y)
            self.snake.append(segment)
            start_x -= 20

    def move_snake(self):
        self.screen.tracer(0)
        self.change_direction()
        while True:
            time.sleep(0.1)
            self.screen.update()
            if not self.check_live():
                print("Game Over")
                break
            for i in reversed(range(1,len(self.snake))):
                t_x,t_y = self.snake[i - 1].pos()
                self.snake[i].goto(t_x,t_y)
            self.snake[0].forward(20)
        # self.screen.exitonclick()

    def change_direction(self):
        self.screen.listen()
        self.screen.onkeypress(key="w", fun=lambda: self.change_dir("UP"))
        self.screen.onkeypress(key="s", fun=lambda: self.change_dir("DOWN"))
        self.screen.onkeypress(key="d", fun=lambda: self.change_dir("RIGHT"))
        self.screen.onkeypress(key="a", fun=lambda: self.change_dir("LEFT"))

    def change_dir(self, direction):
        if direction == "UP":
            if self.snake[0].heading() != 270:
                self.snake[0].setheading(90)
        elif direction == "DOWN":
            if self.snake[0].heading() != 90:
                self.snake[0].setheading(270)
        elif direction == "RIGHT":
            if self.snake[0].heading() != 180:
                self.snake[0].setheading(0)
        elif direction == "LEFT":
            if self.snake[0].heading() != 0:
                self.snake[0].setheading(180)

    def check_live(self):
        t_x,t_y = self.snake[0].pos()
        return -300 <= t_x <= 300 and -300 <= t_y <= 300

