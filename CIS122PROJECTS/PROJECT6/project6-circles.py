# project6-circles.py

import random as r
import turtle as t

color_list = ['cyan', 'blue', 'purple', 'green', 'magenta', 'yellow', 'red', 'lime']
def rand_color(c_list):
    c_len = len(color_list)
    r_color = r.randrange(0, c_len)
    return color_list[r_color]
t.screensize(200, 200)
circle_amt = r.randint(20, 60)
for i in range(circle_amt):
    r_radius = r.randint(10, 60)
    r_x = r.randint(-200, 200)
    r_y = r.randint(-200, 200)
    t.speed('fastest')
    t.penup()
    t.goto(r_x, r_y)
    t.pendown()
    t.fillcolor(rand_color(color_list))
    t.begin_fill()
    t.circle(r_radius)
    t.end_fill()
    
