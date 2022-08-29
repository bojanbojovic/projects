from tkinter import *
import random

class SudokuIntefrace:
    def __init__(self, listOfNumbers):
        self.listOfNumbers = listOfNumbers
        self.window = Tk()
        self.window.title("Sudoku")
        self.window.config(bg="white")
        self.window.geometry("225x300")
        self.entries = []
        self.listOfEntry = []
        self.createButton()

        self.window.mainloop()

    def createButton(self):
        self.button = Button(text="Start", command=self.createSudoku)
        self.button.place(x=80, y=100)

    def createGrid(self):
        self.button.destroy()
        x = 25
        for i in range(1, 9):
            if i % 3 == 0:
                width = 3
            else:
                width = 1

            self.vertical = Frame(self.window, bg="black", height=225, width=width)
            self.vertical.place(x=x, y=0)
            x += 25

        y = 25
        for i in range(1, 10):
            if i % 3 == 0:
                height = 3
            else:
                height = 1

            self.horizontal = Frame(self.window, bg="black", height=height, width=225)
            self.horizontal.place(x=0, y=y)
            y += 25

        self.button = Button(text="Check", command=self.checkSudoku)
        self.button.place(x=70, y=250)

    def createSudoku(self):
        listOfCords = self.getCords()
        i = 80
        listOfNum = []
        for j in range(81):
            listOfNum.append(j)

        for j in range(38):
            num = random.choice(listOfNum)
            listOfNum.remove(num)
            self.listOfEntry.append(num)
            self.entry = Entry(self.window)
            self.entry.place(x=listOfCords[num][0], y=listOfCords[num][1], width=25)
            self.entries.append(self.entry)
            i -= 1

        for j in range(43):
            num = random.choice(listOfNum)
            listOfNum.remove(num)
            self.text = Text(self.window, height=1, width=2)
            self.text.insert(INSERT, self.listOfNumbers[num // 9][num % 9])
            self.text.place(x=listOfCords[num][0], y=listOfCords[num][1])
            i -= 1
        self.createGrid()

    def getCords(self):
        listOfCord = []
        x = 0
        y = 0
        for i in range(10):
            for j in range(10):
                listOfCord.append((y, x))
                y += 25
                if y == 225:
                    y = 0
                    break
            x += 25
            if x == 225:
                break

        return listOfCord

    def checkSudoku(self):
        i = 0
        succesfull = True
        for num in self.listOfEntry:
            entry = self.entries[i]
            if not entry.get() == str(self.listOfNumbers[num // 9][num % 9]):
                succesfull = False
                break
            i += 1

        for ele in self.window.winfo_children():
            ele.destroy()

        text = Text(self.window, height=1, width=7)
        if succesfull:
            text.insert(INSERT, "SUCCESS")
        else:
            text.insert(INSERT, "FAILURE")

        text.place(x=80, y=150)
