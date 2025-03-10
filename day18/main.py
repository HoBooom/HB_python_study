import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()  # 터틀 팬 숨기기
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)  # 초기 터틀 값
number_of_dots = 100   # 내가 그릴 점의 갯수

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # 20 크기 만큼의 점을 찍는다.
    tim.forward(50)  # 50 만큼 앞으로 전진

    if dot_count % 10 == 0:
        tim.setheading(90)  # 90도(위를 향하는 방향)
        tim.forward(50)  # 50만큼 위로 올라감
        tim.setheading(180)  # 180도(왼쪽을 향하는 방향)
        tim.forward(500)  # 500만큼 전진
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
# import turtle as turtle_mode
# from turtle import *
# #from hirst_painting import rgb_colors
# import random

# turtle_mode.colormode(255)
# tim = Turtle()
# tim.up()
# tim.setheading(225)
# tim.forward(500)


# cnt_x, cnt_y = tim.pos()
# start_x = cnt_x
# cnt_color = 0

# rgb_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
#               (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
#               (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
#               (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
#               (176, 192, 209)]

# for x in range(10):
#     cnt_x = start_x
#     for y in range(10):
#         tim.setpos(cnt_x, cnt_y)
#         cnt_x += 50
#         tim.dot(10,random.choice(rgb_colors))
#         cnt_color = (cnt_color + 1) % 30
#     cnt_y += 50



# 스피로 그래프 그리기
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat","SlateGray","SeaGreen"]
# color_n = 0
# head_direction = 0
# tim.speed(10)
# tim.width(3)
# start_head_direct = tim.heading()
# while True:
#     tim.circle(100)
#     head_direction += 20
#     tim.setheading(head_direction)
#     tim.color(colors[color_n])
#     color_n = (color_n + 1) % 8
#     if tim.heading() == start_head_direct:
#         break

# 거북이 무작위행보 그리기
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat","SlateGray","SeaGreen"]
# color_n = 0
# random_degree = [90,180,270,360]
# tim.width(10)
# tim.speed(7)

# while True:
#     tim.color(colors[color_n])
#     color_n = (color_n + 1) % 8
#     tim.setheading(random.choice(random_degree))
#     tim.forward(30)


# screen = Screen()
# screen.exitonclick()
