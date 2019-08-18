# p7_TurtleWalk.py

import random as r
import turtle as t

menu = ' Q Quit\n W Walk randomly for 1000 steps\n E Erase screen and walk randomly\n'
print(menu)
prompt = input('Please select one: ').lower()
color_list = ['red', 'blue', 'purple']

def rand_jump():
    rand_x = r.randint(0,200)
    rand_y = r.randint(0,200)
    t.penup()
    t.goto(rand_x,rand_y)
    t.pendown()
def path():
    t.speed('fastest')
    for step in range(1000):
        turn = r.randint(0,9)*36
        t.forward(8)
        t.right(turn)
    t.dot(10)
while prompt == 'q' or 'w' or 'e':
    if prompt == 'e':
        t.reset()
        t.pencolor(color_list[0])
        path()
        rand_jump()
        t.pencolor(color_list[1])
        path()
        rand_jump()
        t.pencolor(color_list[2])
        path()
        prompt = input('Please select one: ').lower()
    if prompt == 'w':
        t.pencolor(color_list[0])
        path()
        rand_jump()
        t.pencolor(color_list[1])
        path()
        rand_jump()
        t.pencolor(color_list[2])
        path()
        prompt = input('Please select one: ').lower()
    if prompt == 'q':
        exit()


