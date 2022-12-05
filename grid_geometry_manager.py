from operator import ne
from tkinter import *

window = Tk()

titleLabel = Label(
    window,
    text="Sign Up",
    font=("impact", 20)
)
titleLabel.grid(row=0, column=0, columnspan=2)

nameLabel = Label(
    window,
    text="Username",
    width=30
)
nameLabel.grid(row=1, column=0)
nameInput = Entry(window, width=30)
nameInput.grid(row=1, column=1)

passwordLabel = Label(
    window,
    text="Password"
)
passwordLabel.grid(row=2, column=0)
passwordInput = Entry(window, width=30)
passwordInput.grid(row=2, column=1)

emailLabel = Label(
    window,
    text="Email"
)
emailLabel.grid(row=3, column=0)
emailInput = Entry(window, width=30)
emailInput.grid(row=3, column=1)

submitButton = Button(
    window,
    text="Submit",
    font=("Consolas", 18)
)
submitButton.grid(row=4, column=0, columnspan=2)

window.mainloop()
