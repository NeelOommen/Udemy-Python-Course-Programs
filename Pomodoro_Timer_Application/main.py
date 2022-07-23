from itertools import tee
from tabnanny import check
from tkinter import *

from matplotlib.pyplot import text


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def placeholder():
    pass

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps

    window.after_cancel(timer)

    #reset timer text
    canvas.itemconfig(timer_text, text="00:00")
    #reset timer label
    top_label.config(text="Timer")
    #reset check marks
    check_marks.config(text="")

    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        top_label.config(text="Break", fg=RED)
    elif reps%2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        top_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        top_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer

    seconds = count%60
    if seconds < 10:
        seconds = "0" + str(seconds)

    minutes = count//60
    if minutes < 10:
        minutes = "0" + str(minutes)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""

        for _ in range(reps//2):
            marks+="✓"

        if reps%2 == 0:
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(bg = YELLOW, padx = 100, pady = 50)


#Timer Label
top_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
top_label.grid(row=0, column=1)


#load image
canvas = Canvas(width = 200, height = 223, bg = YELLOW, highlightthickness = 0)
image_data = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = image_data)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


#Start Button
start_button = Button(text="Start", command=start_timer, highlightthickness = 0)
start_button.grid(row=2, column=0)


#Reset Button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness = 0)
reset_button.grid(row=2, column=2)


#Check Mark Labels
check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()