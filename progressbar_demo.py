from tkinter import *
from tkinter.ttk import *
import time

def startDownload():
    GB = 100
    download = 0
    speed = 1
    while (download < GB):
        time.sleep(0.05)
        progress_bar['value'] += (speed/GB) * 100
        download += speed
        progress.set(str(int((download/GB) * 100)) + "%")
        task.set(str(download) + "/" + str(GB))
        window.update_idletasks()

window = Tk()

progress = StringVar()
task = StringVar()

progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack()

progressLabel = Label(window, textvariable=progress)
progressLabel.pack()

taskLabel = Label(window, textvariable=task)
taskLabel.pack()

downloadButton = Button(window, text="Download", command=startDownload)
downloadButton.pack()

window.mainloop()
