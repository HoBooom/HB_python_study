from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)

#miles input
input_mile = Entry(width=10)
input_mile.insert(END, string="0")
input_mile.grid(row=0, column=1)

mile_label=Label(text="Miles")
mile_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

#convert km
# def convert(input_mile):
#     input_mile = float(input_mile.get())
#     converted_mile = round(input_mile * 1.609,2)
#     return str(converted_mile)

def calculate_but(input_mile):
    # converted_km.delete(1.0,END)
    # converted_km.insert(END, convert(input_mile))
    input_mile = float(input_mile.get())
    converted_mile = round(input_mile * 1.609, 2)
    converted_km.config(text=f"{converted_mile}")

cal_button = Button(text="Calculate", command=lambda : calculate_but(input_mile))
cal_button.grid(row=2, column=1)


# converted_km = Text(width=10,height=1)
# converted_km.insert(END, convert(input_mile))
# converted_km.grid(row=1, column=1)
converted_km = Label(text="0")
converted_km.grid(row=1, column=1)

km_label=Label(text="Km")
km_label.grid(row=1, column=2)



window.mainloop()