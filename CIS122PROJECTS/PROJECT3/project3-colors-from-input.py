# project3-colored-triangles.py

import turtle as t

def jump(distance):
    t.penup()
    t.forward(50)
    t.pendown()
    return None

def draw_triangle(side_length):
    n_sides = 3
    angle = 360 / 3
    for i in range(n_sides):
        t.forward(side_length)
        t.right(angle)
    return None

def color_triangle(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    draw_triangle(side_length)
    t.end_fill()
    return None

t.speed('fastest')
color_input1 = input("color 1: ")
color_input2 = input("color 2: ")
color_input3 = input("color 3: ")
color_input4 = input("color 4: ")
background_input = input("background color: ")
color_list = [color_input1 , color_input2 , color_input3 , color_input4]
n_colors = len(color_list)
v = 0
n = 12
side_length = 45
angle = 360 / 12

for i in range(n):
    color = color_list[v]
    color_triangle(side_length, color)
    v = v + 1
    if v >= n_colors:
        v = 0
    t.right(angle)
    jump(50)
t.bgcolor(background_input)
