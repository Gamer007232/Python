from turtle import *

bgcolor('Black')
hideturtle()
speed(11)
for i in range(301):
    if i % 2 == 0:
        color('cyan')
    else:
        color('magenta')
    forward(i * 3)
    left(91)
done()