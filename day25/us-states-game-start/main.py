import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")

all_states = states_data.state.to_list()
print(all_states)

ans_count = 0
while True:
    answer_state = screen.textinput(title=f"{ans_count}/50 States Correct", prompt="What's another state's name?")
    cnt_data = states_data[states_data["state"] == answer_state]

    if answer_state == "Exit":
        break

    if not cnt_data.empty:
        print(cnt_data.x,cnt_data.y,cnt_data.state)
        cnt_data_index = cnt_data.index
        cnt_data = cnt_data.iloc[0]
        print(cnt_data)
        print(cnt_data["x"],cnt_data["y"],cnt_data["state"])
        temp_turtle = turtle.Turtle()
        temp_turtle.hideturtle()
        temp_turtle.penup()
        temp_turtle.goto(cnt_data["x"], cnt_data["y"])
        temp_turtle.write(cnt_data["state"])
        ans_count += 1

        states_data.drop(cnt_data_index, inplace=True)
    else:
        print("wrong state name")

states_data.to_csv("after_game_50_states.csv")
turtle.mainloop()