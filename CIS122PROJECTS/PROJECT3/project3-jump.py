# project3-jump.py

import turtle as t
def jump(distance):
    """
      Takes the turtle pen up and moves
      it to a location a specified number of units away
      and puts it down
    """
    t.penup()
    t.forward(200)
    t.pendown()
    return None

# TEST
def draw_triangle(side_length):
    n_sides = 3
    angle = 360 / n_sides
    for i in range(n_sides):
        t.forward(side_length)
        t.right(angle)
    return None
draw_triangle(75)

jump(100)

draw_triangle(75)
