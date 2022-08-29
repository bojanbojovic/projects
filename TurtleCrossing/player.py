from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.x = 0
        self.y = -280
        self.penup()
        self.goto((self.x, self.y))
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reachedEnd(self):
        return self.ycor() >= FINISH_LINE_Y

    def restart(self):
        self.goto((self.x, self.y))

