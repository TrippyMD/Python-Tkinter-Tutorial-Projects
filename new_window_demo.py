from tkinter import *

def openWindow():
    new_window = Tk()
    # new_window = Toplevel()
    old_window.destroy()

old_window = Tk()
old_window.geometry("400x160")

button = Button(
    old_window,
    text="Create New Window",
    command=openWindow
)
button.pack()

old_window.mainloop()
