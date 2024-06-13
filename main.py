from tkinter import *
import os

# initializes tkinter 
root = Tk()
root.title("Pomodoro Timer")
root.minsize(1000, 1000)

def update_time():
    pass

# path to image when not hosted locally 
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "pomodoro.png")

# displays the image as background and adds text 
canvas = Canvas(root, width=1000, height=1000)
tomato_image = PhotoImage(file=image_path)
canvas.create_image(500, 500, image=tomato_image)
timer_text = canvas.create_text(500, 500, text="25:00", fill="white", font=("Arial", 50, "bold"))
canvas.pack()

# displays the button to start countdown
button = Button(root, text="Start Timer", font=("Arial", 16, "bold"), bg="white", height=3, width=30, command=update_time)
button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()