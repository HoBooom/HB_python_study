# from turtle import Turtle, Screen
#
# # 거북이 객체 생성
# timmy = Turtle()
#
# # 거북이 모양 및 색상 설정
# timmy.shape("turtle")
# timmy.color("red")
#
# # 화면 설정
# my_screen = Screen()
# my_screen.bgcolor("white")  # 배경색 설정
# my_screen.screensize(600, 600)  # 창 크기 설정
#
# # 화면의 높이 출력
# print(my_screen.canvheight)
#
# # 거북이 움직이기 (100픽셀 전진)
# timmy.forward(100)
#
# # 종료 대기
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemen Name',['Pikachu','Squirtle','charmander'])
table.add_column('Type',['Electric','Water','Fire'])
# table.add_row(['Pikachu','Electiric'])
# table.add_row(['Squirtle','Water'])
# table.add_row(['Charmander','Fire'])
table.align = 'l'
print(table)
