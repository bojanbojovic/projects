from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

try:
    csv = pandas.read_csv("data/word_to_learn.csv")
    df = pandas.DataFrame(data=csv)

except FileNotFoundError:
    csv = pandas.read_csv("data/french_words.csv")
    df = pandas.DataFrame(data=csv)
finally:
    listOfDict = df.to_dict(orient="records")

number = 0
solve = None
num = 0

def begin():
    global number, num
    num += 1
    number = random.randint(0, 100)
    canvas.itemconfig(canvas_image, image=cardFront)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=listOfDict[number]["French"], fill="black")
    sleep(3)

def sleep(count):
    global num
    if count > 0:
        window.after(1000, sleep, count - 1)
    elif num % 2 != 0:
        changeImage()
    else:
        begin()

def changeImage():
    global number, num
    num += 1
    canvas.itemconfig(canvas_image, image=cardBack)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=listOfDict[number]["English"], fill="white")
    sleep(2)

def wrong():
    pass

def right():
    global number
    listOfDict.remove(listOfDict[number])
    df = pandas.DataFrame(data=listOfDict)
    df.to_csv("data/word_to_learn.csv", index=False)

# -----------------------------------UI Setup-------------------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
cardBack = PhotoImage(file="images/card_back.png")
cardFront = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=cardFront)
title = canvas.create_text(400,150, text="Title", font=("Ariel", 20, "italic"))
word = canvas.create_text(400,263, text="Word", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrongImage = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrongImage,command=wrong, highlightthickness=0)
wrongButton.grid(row=1, column=0)

rightImage = PhotoImage(file="images/right.png")
rightButton = Button(image=rightImage,command=right, highlightthickness=0)
rightButton.grid(row=1, column=1)

begin()


window.mainloop()
