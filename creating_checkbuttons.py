from tkinter import *

def display():
    if (x.get() == 1):
        print("You Agreed!!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar()

arrow_photo = PhotoImage(file='double.png')

check_button = Checkbutton(
    window,
    text="I Agree to the terms and conditions",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    font=("MV Boli", 25),
    image=arrow_photo,
    compound="left",
    padx=25,
    pady=10
)
check_button.pack()

window.mainloop()
