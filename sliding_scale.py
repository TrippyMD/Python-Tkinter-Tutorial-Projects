from tkinter import *

def showValue():
    print(f"Temperature:  {str(scale_slide.get())} degrees C")

window = Tk()

hotImage = PhotoImage(file='arrow.png')
hotLabel = Label(
    image=hotImage
)
hotLabel.pack()

scale_slide = Scale(
    window,
    from_=100,
    to=0,
    length=600,
    orient=VERTICAL,
    tickinterval=10,
    troughcolor="lightblue",
    font=("Ink Free", 20),
    showvalue=10, # Set to 0 to stop showing scale value
    resolution=5, # Increment of slider
    fg="red",
    bg="white",
    highlightbackground="green",
    highlightcolor="purple",

)
scale_slide.set(((scale_slide["from"] - scale_slide["to"])/2) + scale_slide["to"])
scale_slide.pack()

coldImage = PhotoImage(file='skull.png')
coldLabel = Label(
    image=coldImage
)
coldLabel.pack()

button = Button(
    window,
    text="submit",
    command=showValue,
    font=("Ink Free", 20)
)
button.pack()

window.mainloop()
