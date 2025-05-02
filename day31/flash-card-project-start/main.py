from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORD = './data/french_words.csv'
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(FRENCH_WORD)
    print(original_data)
    to_learn = original_data.to_dict('records')
else:
    to_learn = data.to_dict('records')

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, lambda : filp_card())

def filp_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, lambda : filp_card())

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_btn.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_btn = Button(image=check_image,highlightthickness=0,command=is_known)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()



# french_data_frame = pd.read_csv(FRENCH_WORD)
# word_dict = french_data_frame.to_dict(orient="records")
#
#
# def back_func(english):
#     canvas.itemconfig(card_front, image=card_back_image)
#     canvas.itemconfig(card_title, text="english",fill="white")
#     canvas.itemconfig(card_word, text=english,fill="white")
#
# def wrong_random_word():
#     word = random.choice(word_dict)
#     french = word["French"]
#     english = word["English"]
#     canvas.itemconfig(card_front, image=card_front_image)
#     canvas.itemconfig(card_title, text="french",fill="black")
#     canvas.itemconfig(card_word, text=french,fill="black")
#
#     window.after(3000, lambda: back_func(english))
#
# def check_random_word():
#     word = random.choice(word_dict)
#     french = word["French"]
#     english = word["English"]
#     canvas.itemconfig(card_front, image=card_front_image)
#     canvas.itemconfig(card_title, text="french",fill="black")
#     canvas.itemconfig(card_word, text=french,fill="black")
#
#
#
#     window.after(3000, lambda: back_func(english))
#
#
# window = Tk()
# window.title("Flash Card Project")
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
# card_front_image = PhotoImage(file="./images/card_front.png")
# wrong_btn_image = PhotoImage(file="./images/wrong.png")
# right_btn_image = PhotoImage(file="./images/right.png")
# card_back_image = PhotoImage(file="./images/card_back.png")
#
# canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightthickness=0)
# card_front = canvas.create_image(400,263,image=card_front_image)
# card_title = canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"), fill="black")
# card_word = canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"), fill="black")
#
#
#
# wrong_btn = Button(image=wrong_btn_image,highlightthickness=0,borderwidth=0, command=wrong_random_word)
# right_btn = Button(image=right_btn_image,highlightthickness=0,borderwidth=0, command=check_random_word)
#
#
# canvas.grid(row=0, column=0, columnspan=2)
# wrong_btn.grid(row=1, column=0)
# right_btn.grid(row=1, column=1)
#
# window.mainloop()