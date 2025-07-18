from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#695355"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps  = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER")
    check_marks.config(text="") 
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        
        if reps < 8:  # Optional: Stop after 4 work sessions
            start_time()

        work_sessions = math.floor(reps / 2)
        marks = "✔" * work_sessions
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg="#695355")

title_label = Label(text="TIMER", bg =GREEN, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=400, height=400, bg="#695355")
tomato_image= PhotoImage(file="C:\\Users\\PRATHAM\\tomato.png")
canvas.create_image(150, 200, image=tomato_image)
timer_text = canvas.create_text(100, 80, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="START", highlightbackground=PINK, command=start_time)
start_button.grid(column=0, row=2)


reset_button = Button(text="RESET", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, font=(FONT_NAME, 40))
check_marks.grid(column=3, row=2)

window.mainloop()