from tkinter import *

def submit():

    fruits = []

    for index in listbox.curselection():
        fruits.insert(index, listbox.get(index))

    print("You will eat:  ")
    for index in fruits: 
        print(index)

def addFruit():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())
    entry.delete(0, END)

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    # listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(
    window,
    font=("Papyrus", 20),
    width=20,
    selectmode=MULTIPLE
)
listbox.pack()

listbox.insert(1, "Orange")
listbox.insert(2, "Banana")
listbox.insert(3, "Apple")
listbox.insert(4, "Mangoe")
listbox.insert(5, "PawPaw")

listbox.config(height=listbox.size())

entry = Entry(
    window,
    font=("Papyrus", 18)
)
entry.pack()

add_button = Button(
    window,
    text="add",
    command=addFruit,
    font=("Papyrus", 17)
)
add_button.pack()

submit_button = Button(
    window,
    text="Submit",
    command=submit,
    font=("Papyrus", 17)
)
submit_button.pack()

delete_button = Button(
    window,
    text="Delete",
    command=delete,
    font=("Papyrus", 17)
)
delete_button.pack()

window.mainloop()
