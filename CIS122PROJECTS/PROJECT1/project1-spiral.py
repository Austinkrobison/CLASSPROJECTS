
# project1-spiral.py

import turtle
turtle.pencolor('cyan')
def spiral(n, angle, step):
    for step in range(n):
        turtle.forward(step)
        turtle.left(angle)
spiral(120,60,10)
