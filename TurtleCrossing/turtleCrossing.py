import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()

cars = []

screen.listen()
screen.onkey(fun=player.move, key="Up")

speed = 5
car = CarManager(speed)
cars.append(car)
gameIsOn = True
j = 0
while gameIsOn:
    time.sleep(0.1)
    screen.update()
    if j % 5 == 0:
        car = CarManager(speed)
        cars.append(car)

    for i in cars:
        if i.headOfCar.xcor() < -280:
            i.remove()
            cars.remove(i)

    for i in cars:
        i.move()

    if player.reachedEnd():
        player.restart()
        score.updateScore()
        for i in cars:
            speed = i.incrementSpeed()

    for i in cars:
        if player.distance(i.headOfCar) < 20 or player.distance(i.tailOfCar) < 20:
            gameIsOn = False
            score.printEndGame()
            break

    j += 1

screen.exitonclick()


