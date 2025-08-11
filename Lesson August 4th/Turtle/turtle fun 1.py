from turtle import *
import os
import time

speed(5)
bgcolor("black")
color("greenyellow")
pensize(5)

for i in range(8):
    left(45)
    for i in range(8):
        forward(100)
        left(45)

hideturtle()

time.sleep(8)
os.system('cls')

for i in range(6):
    left(60)
    for i in range(6):
        forward(100)
        left(60)
