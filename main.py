import time
from tkinter import *

root = Tk()
root.title("Pomodoro Timer")
root.minsize(1000, 1000)


def update_time():
    print("Clicked")


button = Button(text = "Start Timer", command = update_time) 
button.pack()

root.mainloop()