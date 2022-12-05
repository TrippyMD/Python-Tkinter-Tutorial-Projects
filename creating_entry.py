from curses import window
from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(
    window,
    fg="#00FF00",
    bg="black",
    font=("Ink Free", 26, "bold")
)
# entry.insert(0, "Spongebob")
# entry.config(show="*", state=DISABLED)
entry.pack(side=LEFT)

submit_button = Button(
    window,
    text="Submit",
    command=submit
)
submit_button.pack(side=RIGHT)

delete_button = Button(
    window,
    text="Delete",
    command=delete
)
delete_button.pack(side=RIGHT)

backspace_button = Button(
    window,
    text="Backspace",
    command=backspace
)
backspace_button.pack(side=RIGHT)

window.mainloop()
