from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.writeScore()

    def writeScore(self):
        self.color("black")
        self.hideturtle()
        self.goto(-230, 270)
        self.write("Level: 1", False, align="center", font=FONT)

    def updateScore(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, align="center", font=FONT)

    def printEndGame(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=FONT)