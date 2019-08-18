# project2-triangles

import turtle as t

n = 45

def draw_triangle(size):
    """draw_triangle(size)
       Uses the given size to draw an equilateral triangle
       return None
    """
    n_sides = 3
    angle = 360 / n_sides
    for count in range(n_sides):
        t.forward(size)
        t.left(angle)
    return None

t.speed('fastest')
t.pencolor('red')

size = 3
extra = 2

draw_triangle(20)
draw_triangle(50)
draw_triangle(70)

for i in range(n):
    draw_triangle(size)
    size = size + extra
    t.right(7)
    t.forward(5)

