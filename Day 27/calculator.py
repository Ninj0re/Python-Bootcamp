from tkinter import *


window = Tk()
window.minsize(width=300, height=150)

title_label = Label(text="Foot to Meter Calculator")
title_label.grid(column=0, row=0)
title_label.config(padx=50)

meter_result = Label()
meter_result.grid(column=0, row=1)
meter_result.config(pady=20)
meter_label = Label(text="meter")
meter_label.grid(column=1, row=1)

foot_entry = Entry()
foot_entry.grid(column=0, row=2)
title_label = Label(text="foot")
title_label.grid(column=1, row=2)


def calculate():
    meter_result.config(text=float(foot_entry.get()) * 0.304800004)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=0, row=4, pady=20)
calculate_button.config()


window.mainloop()
