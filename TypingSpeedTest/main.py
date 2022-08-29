from tkinter import *
import random
import time


def getWords():
    listOfWords = []
    with open(file="english-word-list-total.csv") as file:
        words = file.read().split(";")
        for i in words[1::3]:
            listOfWords.append(i)
    return listOfWords


listOfWords = getWords()
beginningWords = []
for i in range(15):
    beginningWords.append(listOfWords[random.randint(0, 500)])

textWords = " ".join(beginningWords)
i = [0]
j = 0
numOfTrue = [0]
numOfFalse = [0]
numOfWords = [0]
timeout = time.time() + 60

def click(key):
    global listOfWords, beginningWords, i, numOfTrue, numOfFalse, numOfWords, timeout

    if time.time() > timeout:
        input.unbind("<Key>")
        input.destroy()
        wpm = numOfWords[0]
        canvas.itemconfig(words, text=f"Your score: {wpm} WPM")

    word = beginningWords[0]
    char = key.char

    if char == " ":
        if numOfTrue[0] == len(word) and numOfFalse[0] == 0:
            numOfWords[0] += 1
        input.delete(0, "end")
        temp = list(beginningWords[1:])
        temp.append(listOfWords[random.randint(0, 500)])
        beginningWords = temp
        textWords = " ".join(temp)
        canvas.itemconfig(words, text=textWords)
        numOfFalse[0] = 0
        numOfTrue[0] = 0
        i[0] = 0
    elif i[0] < len(word) and char == word[i[0]]:
        numOfTrue[0] += 1
        i[0] += 1
    else:
        numOfFalse[0] += 1


window = Tk()
window.title("TypingSpeed")
# window.geometry("600x300")

canvas = Canvas(width=600, height=200, highlightthickness=0)
words = canvas.create_text(280, 100, width=500, text=textWords, font=("Arial", 15, "bold"), fill="black")
canvas.grid(row=0, column=0)

input = Entry()
input.grid(row=1, column=0)
input.focus_set()
input.bind("<Key>", click)


window.mainloop()
