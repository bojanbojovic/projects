from turtle import Turtle

class Padle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto((self.x, self.y))

    def up(self):
        self.y += 20
        self.goto((self.x, self.y))

    def down(self):
        self.y -= 20
        self.goto((self.x, self.y))




