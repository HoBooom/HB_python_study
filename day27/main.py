import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#Label
my_label = tkinter.Label(text="First State", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    print("Button clicked")
    # new_text = input.get()
    # my_label.config(text=new_text)


#Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

button = tkinter.Button(text="Quit", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="NewButton", command=button_clicked)
new_button.grid(column=2, row=0)




window.mainloop()

