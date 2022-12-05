from tkinter import *
from tkinter import filedialog

def saveText():
    file = filedialog.asksaveasfile(
        initialdir="/",
        filetypes=[
            ("Text File", ".txt"),
            ("HTML File", ".html"),
            ("All Files", ".*")
        ]
    )
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()
    

window = Tk()

button = Button(
    window,
    text="Save",
    command=saveText
)
button.pack()

text = Text(
    window
)
text.pack()

window.mainloop()
