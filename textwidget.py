from tkinter import *

def submit():
    words = text.get("1.0", END)
    print(words)

window = Tk()

text = Text(
    window,
    font=("Ink Free", 17),
    bg="light yellow",
    height=8,
    width=20,
    padx=10,
    pady=10,
    fg="purple"
)
text.pack()

button = Button(
    window,
    text="Submit",
    font=("impact", 14),
    command=submit
)
button.pack()

window.mainloop()
