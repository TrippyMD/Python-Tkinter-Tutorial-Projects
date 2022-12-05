from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_move(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()
window.geometry("400x400")

label = Label(window, bg="red", width=20, height=10)
label.place(x=0, y=0)
label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_move)

label2 = Label(window, bg="blue", width=20, height=10)
label2.place(x=100, y=60)
label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_move)

window.mainloop()
