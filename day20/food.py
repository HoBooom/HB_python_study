import random

class Food:
    def __init__(self):
        self.food_x = None
        self.food_y = None
        self.food = False

    def make_food(self):
        self.food_x = random.randint(-300, 300)
        self.food_y = random.randint(-300, 300)
        self.food = True


