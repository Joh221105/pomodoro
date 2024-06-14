from tkinter import *
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# initializes tkinter 
root = Tk()
root.title("Pomodoro Timer")
root.minsize(1000, 1000)

session = 1

# function to play sound when session is over
def play_sound():
    pygame.mixer.music.load("./finish.wav")  # Replace with your audio file
    pygame.mixer.music.play()

def determine_session():
    global session
  
    # turns minutes into seconds
    work_time = 5
    short_break = 5 * 60  
    long_break = 20 * 60  
    
    # determines the length of the session
    if session % 8 == 0:
        update_time(long_break)
    elif session % 2 == 0:
        update_time(short_break)
    else:
        update_time(work_time)
    
    session += 1

# imitates the countdown and updates the display using recursion
def update_time(count):
    if count >= 0:
        mins, secs = divmod(count, 60)
        time_format = f'{mins:02}:{secs:02}'
        canvas.itemconfig(timer_text, text=time_format)
        count -= 1
        root.after(1000, update_time, count)
    else:
        play_sound()

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
button = Button(root, text="Start Timer", font=("Arial", 16, "bold"), bg="white", height=3, width=30, command=determine_session)
button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()