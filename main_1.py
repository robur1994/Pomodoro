from tkinter import *
import math
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
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_taimer.config(text="Timer", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=GREEN)
    check_button.config(fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        label_taimer.config(text="Work", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_taimer.config(text="Break", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=RED)
    else:
        count_down(short_break_sec)
        label_taimer.config(text="Break", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=PINK)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"

        check_button.config(text=mark, font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=58, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
picture = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=picture)
timer_text = canvas.create_text(100, 138, text="00:00", fill = "white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=2, row=2)

label_taimer =Label(text="Timer", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=GREEN)
label_taimer.grid(column=2, row=0)

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=3)
button_Reset = Button(text="Reset", command=reset_timer)
button_Reset.grid(column=3, row=3)

check_button = Label(fg=GREEN, bg=YELLOW)
check_button.grid(column=2, row=4)







window.mainloop()
