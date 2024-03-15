import tkinter


window = tkinter.Tk()
window.title("Deneme")
window.minsize(width=500, height=300)

label = tkinter.Label(text="0")
label.pack()


def increase_value():
    try:
        label["text"] = int(label["text"]) + 1
    except:
        label.config(text=0)


tkinter.Button(text="Click!", command=increase_value).pack()

tkinter.Label(text="--------------------------------------------------------------------").pack()

entry = tkinter.Entry()
entry.pack()


def get_value():
    label.config(text=entry.get())


tkinter.Button(text="Click!", command=get_value).pack()


window.mainloop()
