from tkinter import *
from tkinter import messagebox

def showBox():
    # messagebox.showinfo(title="Important Info", message="Update your OS!")
    # messagebox.showwarning(title="WARNING", message="You've been warned")
    # messagebox.showerror(title="ERRoR", message="OS under VIRUS threat!!")

    # if messagebox.askokcancel(title="Ask", message="Are you sure you want to quit?"):
        # print("You Exited!!")
    # else:
        # print("You did not quit!!")

    # answer = messagebox.askquestion(title="Quiz", message="Have you watched Breaking Bad?")
    # if (answer=="yes"):
        # print("Best show ever, right?")
    # elif (answer=="no"):
        # print("Go watch it, I highly recommend that..")

    # if messagebox.askretrycancel(title="Retry", message="Failed! Do you want to retry?"):
        # print("Retrying")
    # else:
        # print("Failed to download!!")

    # if messagebox.askyesno(title="Choose or else", message="Are you a virgin?"):
        # print("Yay Virgin..Good for you")
    # else:
        # print("Always use protection, always!")

    marry_me = messagebox.askyesnocancel(title="Weddings", message="Do you take me to be your lawfully wedded husband?")
    if marry_me:
        print("Yes I Do :)")
    elif (marry_me == False):
        print("No! I Don't")
    else:
        print("Hell No!!!")

window = Tk()
window.geometry("300x300")

Button(window, text="Show Me", command=showBox, font=("impact", 20)).pack()

window.mainloop()
