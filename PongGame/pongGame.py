from turtle import Screen
from padle import Padle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

rPadle = Padle(350, 0)
lPadle = Padle(-350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=rPadle.up, key="Up")
screen.onkey(fun=rPadle.down, key="Down")
screen.onkey(fun=lPadle.up, key="w")
screen.onkey(fun=lPadle.down, key="s")

gameIsOn = True
while gameIsOn:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.distance(rPadle) < 50 and ball.xcor() > 320 or ball.distance(lPadle) < 50 and ball.xcor() < -320:
        ball.bounceX()


    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.lPoint()

    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rPoint()
    



screen.exitonclick()
