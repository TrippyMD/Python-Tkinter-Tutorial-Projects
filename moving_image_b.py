from tkinter import *

def move_up(event):
    canvas.move(skull, 0, -10)

def move_down(event):
    canvas.move(skull, 0, +10)

def move_left(event):
    canvas.move(skull, -10, 0)

def move_right(event):
    canvas.move(skull, +10, 0)

window = Tk()

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

photoimage = PhotoImage(file="skull.png")

canvas = Canvas(window, width=500, height=500)
canvas.pack()

skull = canvas.create_image(0, 0, image=photoimage, anchor=NW)

window.mainloop()
