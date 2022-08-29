from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self, speed):
        super().__init__()
        self.speedOfCar = speed
        self.car = []
        self.generateCar()
        self.headOfCar = self.car[0]
        self.tailOfCar = self.car[1]

    def generateCar(self):
        self.x = 280
        self.y = random.randint(-280, 280)
        color = random.choice(COLORS)
        for i in range(2):
            mashine = Turtle("square")
            mashine.color(color)
            mashine.penup()
            mashine.goto((self.x, self.y))
            self.car.append(mashine)
            self.x -= 20

    def move(self):
        for i in self.car:
            i.backward(self.speedOfCar)

    def incrementSpeed(self):
        self.speedOfCar += MOVE_INCREMENT
        return self.speedOfCar

    def remove(self):
        for i in self.car:
            i.hideturtle()



