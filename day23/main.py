import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
screen.listen()
screen.onkeypress(key="w",fun=player.move_up)

temp = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    if car_manager.boom(player):
        game_is_on = False
        scoreboard.game_over()

    if player.is_end_line():
        player.go_start_line()
        car_manager.clear_cars()
        scoreboard.next_stage()
        car_manager.speed_up()

screen.exitonclick()