from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(f"Count: {count}")

window = Tk()

icon = PhotoImage(file='skull.png')

button = Button(window,
    text="Click Me!",
    command=click,
    font=("Papyrus", 30, "bold"),
    bg="black",
    fg="#00FF00",
    activebackground="#00FF00",
    activeforeground="black",
    state=ACTIVE,
    image=icon,
    compound="bottom"
)
button.pack()

window.mainloop()
