import math
from tkinter import *
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
timerT = None

# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    global timerT
    window.after_cancel(timerT)
    timer.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(timerText, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    workSek = WORK_MIN * 60
    shortBreakSek = SHORT_BREAK_MIN * 60
    longBreakSek = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0 :
        countDown(longBreakSek)
        timer.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        countDown(workSek)
        timer.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        countDown(shortBreakSek)
        timer.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    min = math.floor(count / 60)
    sek = count % 60
    if sek < 10:
        sek = f"0{sek}"

    canvas.itemconfig(timerText, text=f"{min}:{sek}")
    if count > 0:
        global timerT
        timerT = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        marks = ""
        workSession = math.floor(reps / 2)
        for i in range(workSession):
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoPicture = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomatoPicture)
timerText = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)


timer = Label(text="Timer", font=(FONT_NAME, 25, "normal"), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

start = Button(text="Start", command=startTimer, highlightthickness=0)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=resetTimer, highlightthickness=0)
reset.grid(row=2, column=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)


window.mainloop()
