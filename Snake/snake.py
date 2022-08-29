from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        x = 0
        y = 0
        for i in range(3):
            snakic = Turtle("square")
            snakic.color("white")
            snakic.penup()
            snakic.goto(x, y)
            self.segments.append(snakic)
            x -= 20

    def extend(self):
        snakic = Turtle("square")
        snakic.color("white")
        snakic.penup()
        snakic.goto(self.segments[-1].position())
        self.segments.append(snakic)


    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segment - 1].xcor()
            newY = self.segments[segment - 1].ycor()
            self.segments[segment].goto(newX, newY)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]
