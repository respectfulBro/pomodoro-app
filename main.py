from itertools import count
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Papyrus"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    if reps % 8 == 0 and reps != 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 != 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=GREEN)
    elif reps % 2 == 0:
        countdown(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=PINK)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps
    global timer
    if count == LONG_BREAK_MIN * 60 or count == SHORT_BREAK_MIN * 60 or count == WORK_MIN * 60:
        count_temp = f"{int(count / 60)}:00"
    elif count % 60 < 10:
        count_temp = f"{int(count / 60)}:0{count % 60}"
    elif count < 10:
        count_temp = f"{int(count / 60)}0:0{count % 60}"
    elif count < 60:
        count_temp = f"{int(count / 60)}0:{count % 60}"
    else:
        count_temp = f"{int(count / 60)}:{count % 60}"
    canvas.itemconfig(timer_text, text=count_temp)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for i in range(int(reps / 2)):
            marks += "✔"
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, highlightthickness=0, bg=YELLOW, font=("Papyrus", 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(fg=GREEN, highlightthickness=0, bg=YELLOW, font=("Papyrus", 20, "bold"))
tick_label.grid(column=1, row=3)

window.mainloop()
