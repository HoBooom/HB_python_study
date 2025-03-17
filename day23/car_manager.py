from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def speed_up(self):
        self.move_speed += self.move_increment

    def move_cars(self):
        for car in self.all_cars:
            car.goto(car.xcor() - self.move_speed, car.ycor())

    def boom(self, player):
        for car in self.all_cars:
            if car.distance(player) < 20:
                return True
        return False

    def clear_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()

