from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leftPadle = 0
        self.rightPadle = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto((-100, 200))
        self.write(self.leftPadle, align="center", font=("Courier", 50, "normal"))
        self.goto((100, 200))
        self.write(self.rightPadle, align="center", font=("Courier", 50, "normal"))

    def lPoint(self):
        self.leftPadle += 1
        self.updateScoreboard()

    def rPoint(self):
        self.rightPadle += 1
        self.updateScoreboard()
