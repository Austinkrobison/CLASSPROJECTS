# Project3-draw-poly.py

import turtle as t

def jump(distance):
    t.penup()
    t.forward(50)
    t.pendown()
    return None

def draw_poly(side_length, n_sides):
    angle = 360 / n_sides
    for i in range(n_sides):
        t.forward(side_length)
        t.right(angle)
    return None

def color_poly(side_length, n_sides, color):
    t.fillcolor(color)
    t.begin_fill()
    draw_poly(side_length, n_sides)
    t.end_fill()
    return None

n_sides = int(input('Number of desired sides: '))
t.speed('fastest')
shape_amount = int(input('Number of desired shapes: '))
color_input1 = input('Desired color 1 (of 4): ')
color_input2 = input('Desired color 2 (of 4): ')
color_input3 = input('Desired color 3 (of 4): ')
color_input4 = input('Desired color 4 (of 4): ')
background_input = input('Desired background color: ')
color_list = [color_input1, color_input2, color_input3, color_input4]
n_colors = len(color_list)
v = 0
n = 12
side_length = 200 / n_sides
angle = 360 / shape_amount

for color in range(n):
    color = color_list[v]
    color_poly(side_length, n_sides, color)
    v = v + 1
    if v >= n_colors:
        v = 0
    t.right(angle)
    jump(50)
t.bgcolor(background_input)

