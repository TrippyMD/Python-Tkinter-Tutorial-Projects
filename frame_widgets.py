from curses import window
from tkinter import *

window = Tk()
window.geometry("500x500")

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.pack()

Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()
