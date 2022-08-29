from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.xMove = 10
        self.yMove = 10
        self.shape("circle")
        self.penup()
        self.color("red")
        self.movespeed = 0.1

    def move(self):
        self.x += self.xMove
        self.y += self.yMove
        self.goto((self.x, self.y))

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1
        self.movespeed *= 0.9

    def resetPosition(self):
        self.x = 0
        self.y = 0
        self.bounceX()
        self.movespeed = 0.1




