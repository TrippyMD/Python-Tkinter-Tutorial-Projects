from tkinter import *
from tkinter import filedialog

def submit():
    filepath = filedialog.askopenfilename(initialdir="/",
        title="Open Text File",
        filetypes=(("text files", "*.txt"),("all files", "*.*"))
    )
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(
    window,
    text="Open File",
    command=submit
)
button.pack()

window.mainloop()
