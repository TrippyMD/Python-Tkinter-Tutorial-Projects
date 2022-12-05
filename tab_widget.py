from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

tab1 = Frame(window)
tab2 = Frame(window)

notebook.add(tab1, text="tab 1")
notebook.add(tab2, text="tab 2")

Label(tab1, text="you are in tab number #1", width=50, height=25).pack()
Label(tab2, text="you are in tab number #2", width=50, height=25).pack()

window.mainloop()
