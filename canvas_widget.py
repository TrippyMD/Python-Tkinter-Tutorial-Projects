from tkinter import *

window = Tk()

canvas = Canvas(window, width=500, height=500)
# canvas.create_line(0,0,500,500,width=5)
# canvas.create_line(0,500,500,0,fill="blue",width=5)
# canvas.create_rectangle(50, 50, 350, 250, fill="purple", width=10)
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points, fill="yellow", width=4, outline="red")
# canvas.create_arc(0,0,500,500, fill="lightblue", width=5, style=PIESLICE, start=180, extent=180)

canvas.create_arc(0,0,500,500, fill="red", extent=180, width=8)
canvas.create_arc(0,0,500,500, fill="white", extent=180, width=8, start=180)
canvas.create_oval(190,190,310,310, fill="white", width=8)

canvas.pack()

window.mainloop()
