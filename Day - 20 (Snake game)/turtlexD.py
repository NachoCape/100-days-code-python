
from turtle import Turtle, Screen
import time
import random

tortuguitaxD = Turtle()
tortuguitaxD.shape("turtle")
tortuguitaxD.color("red")
circulitoxD = Turtle()
circulitoxD.color("yellow")
circulitoxD.shape("circle")
tortuguitaxD.penup()
circulitoxD.penup()
circulitoxD.goto(100, 0)
tortuguitaxD.goto(-100,0)
tortuguitaxD.speed(10)

def ramdom_color():
    r = random.randint(0, 255)
    g  = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

tortuguitaxD.left(90)
circulitoxD.right(90)

screen.listen()
screen.onkey(tortuguitaxD.up,"Up")
screen.onkey(tortuguitaxD.down,"Down")
screen.onkey(circulitoxD.up, "Up")
screen.onkey(circulitoxD.down, "Down")

while True:
    if not tortuguitaxD.ycor() <= 100 or not tortuguitaxD.ycor() >= -100 :
        tortuguitaxD.right(180)
    if not circulitoxD.ycor() <= 100 or not circulitoxD.ycor() >= -100:
        circulitoxD.right(180)
    # tortuguitaxD.forward(100)
    # circulitoxD.forward(100)
