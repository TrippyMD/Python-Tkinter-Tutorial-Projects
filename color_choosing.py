from tkinter import *
from tkinter import colorchooser

def changeColor():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(background=colorHex)
    button.config(bg=colorHex, activebackground=colorHex)

window = Tk()
window.geometry("420x450")

button = Button(
    window,
    text="Choose Backgound",
    command=changeColor,
    font=("Papyrus", 15)
)
button.pack()

window.mainloop()
