import pandas as pd
#
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# fur_color = data["Primary Fur Color"]
# print(fur_color)
#
# new_data = {
#     "Fur Color" : ["grey","red","black"],
#     "Count" :[0,0,0]
# }
#
# for color in fur_color:
#     if color == "Gray":
#         new_data["Count"][0] += 1
#     elif color == "Black":
#         new_data["Count"][2] += 1
#     elif color == "Cinnamon":
#         new_data["Count"][1] += 1
#
# print(new_data)
# new_data_pd = pd.DataFrame(new_data)
# new_data_pd.to_csv("new_data.csv")

grey_squirrel = len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"]=="Black"])

data_dic = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count" : [grey_squirrel,red_squirrel,black_squirrel]
}
df = pd.DataFrame(data_dic)
df.to_csv("new_data.csv")

