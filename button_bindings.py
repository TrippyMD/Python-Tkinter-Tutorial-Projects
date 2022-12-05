from tkinter import *

def doSomething(event):
    print(f"Mouse Coordinates: {event.x}, {event.y}")

window = Tk()

# window.bind("<Button-1>", doSomething)
# window.bind("<Button-2>", doSomething)
# window.bind("<Button-3>", doSomething)
# window.bind("<Enter>", doSomething)
# window.bind("<ButtonRelease>", doSomething)
# window.bind("<Leave>", doSomething)
window.bind("<Motion>", doSomething)

window.mainloop()
