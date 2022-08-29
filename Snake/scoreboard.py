from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highScore = int(file.read())
        self.penup()
        self.writeScore()

    def writeScore(self):
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write("Score: 0", False, align="center", font=("Arial",15,"italic"))


    def updateScore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.highScore}", False, align="center", font=("Arial",15,"italic"))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
        with open("data.txt", "w") as file:
            file.write(str(self.highScore))
        self.score = 0
        self.updateScore()

    # def printEndGame(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write("Game Over", False, align="center", font=("Arial", 30, "italic"))

