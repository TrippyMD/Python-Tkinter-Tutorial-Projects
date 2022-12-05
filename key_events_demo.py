from tkinter import *

def doSomething(event):
    label.config(text=event.keysym)

window = Tk()
window.geometry("420x260")

window.bind("<Key>", doSomething)

label = Label(window, font=("Helvetica", 60, "bold"))
label.pack()

window.mainloop()
