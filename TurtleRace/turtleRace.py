from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
turtlesDistance = [0, 0, 0, 0, 0, 0]

y = -100
for i in colors:
    tim = Turtle("turtle")
    tim.penup()
    tim.color(i)
    tim.goto(x=-230, y=y)
    turtles.append(tim)
    y += 35

winner = "red"
toContinue = True
while toContinue:
    for i in range(len(turtles)):
        randDistance = random.randint(0, 10)
        turtles[i].forward(randDistance)
        turtlesDistance[i] += randDistance
        if turtlesDistance[i] >= 450:
            winner = colors[i]
            toContinue = False
            break

if userBet == winner:
    print(f"You Won. Winner is {winner}")
else:
    print(f"You lost. Winner is {winner}")





screen.exitonclick()
