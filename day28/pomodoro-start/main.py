from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_time():
    global reps
    if reps % 2 == 0 and reps != 8:
        canvas.itemconfig(timer_text, fill=GREEN)
        count_down(WORK_MIN * 60)
        check_mark_label.config(text=f"{"✔" * (reps // 2)}")
    elif reps % 2 != 0:
        count_down(SHORT_BREAK_MIN * 60)
        canvas.itemconfig(timer_text, fill=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        canvas.itemconfig(timer_text, fill=RED)
    reps += 1




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    remain_min = count // 60
    remain_sec = count % 60
    if remain_min < 10:
        remain_min = f"0{remain_min}"
    if remain_sec < 10:
        remain_sec = f"0{remain_sec}"
    canvas.itemconfig(timer_text, text=f"{remain_min}:{remain_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



#Timer text
timer_label = Label(text="Timer",font=(FONT_NAME, 40, "bold"),bg=YELLOW, fg=GREEN)
timer_label.grid(row=0,column=1)

check_mark_label = Label(text="✔",font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_mark_label.grid(row=3,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00",fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1,column=1)


start_btn = Button(text="Start", command=start_time, bg=YELLOW, highlightbackground=YELLOW)
start_btn.grid(row=2,column=0)

reset_btn = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightbackground=YELLOW)
reset_btn.grid(row=2,column=2)






window.mainloop()