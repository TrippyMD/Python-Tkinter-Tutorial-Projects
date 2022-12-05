from tkinter import *

def openFile():
    print("You opened a file!!")

def saveFile():
    print("You saved a file!!")

def aboutUs():
    print("We are a tkinter GUI good sir!!")

def helpUs():
    print("We can't help you, sorry.")

window = Tk()

menubar = Menu(
    window
)
window.config(menu=menubar)

fileMenu = Menu(
    menubar,
    tearoff=0
)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


helpMenu = Menu(
    menubar,
    tearoff=0
)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=aboutUs)
helpMenu.add_command(label="Help Center", command=helpUs)

window.mainloop()
