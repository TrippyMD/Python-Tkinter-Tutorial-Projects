from tkinter import *

def order():
    if (x.get() == 0):
        print("You ordered Anarchy")
    elif (x.get() == 1):
        print("You ordered Remenice")
    elif (x.get() == 2):
        print("You ordered Dictator")
    else:
        print("huh?")

window = Tk()

games = ["Anarchy", "Remenice", "Dictator"]

anarchy = PhotoImage(file='skull.png')
remenice = PhotoImage(file='double.png')
dictator = PhotoImage(file='arrow.png')

radio_photos = [anarchy, remenice, dictator]

x = IntVar()

for index in range(len(games)):
    radio_button = Radiobutton(
        window,
        text=games[index],
        variable=x,
        value=index,
        padx=50,
        font=("Poor Richard", 33),
        command=order,
        indicatoron=0,
        width=250,
        image=radio_photos[index],
        compound='left'
    )
    radio_button.pack(anchor=W)


window.mainloop()
