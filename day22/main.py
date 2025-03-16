from turtle import Screen
import player
import time
import ball
import score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong game")
screen.tracer(0)

player1 = player.Player(-350,0)
player2 = player.Player(350,0)
ball1 = ball.Ball()
score = score.Score()

screen.listen()
screen.onkeypress(key="w", fun=player1.move_up)
screen.onkeypress(key="s", fun=player1.move_down)
screen.onkeypress(key="i", fun=player2.move_up)
screen.onkeypress(key="k", fun=player2.move_down)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    ball1.move()

    if ball1.ycor() > 280 or ball1.ycor() < -280:
        ball1.bounce_y()

    if ball1.xcor() > 320 and ball1.distance(player2) < 50:  # 오른쪽 패들
        print("contact")
        ball1.bounce_x()
    elif ball1.xcor() < -320 and ball1.distance(player1) < 50:  # 왼쪽 패들
        print("contact")
        ball1.bounce_x()

    if ball1.xcor() > 380:
        ball1.reset_position()
        score.l_point()
    if ball1.xcor() < -380:
        ball1.reset_position()
        score.r_point()

    screen.update()

