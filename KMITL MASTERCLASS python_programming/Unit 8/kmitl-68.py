# Drawing squares with different colors

from turtle import *
for c in ['red','green','yellow','blue']:
    color(c)
    forward(100)
    right(90)

import turtle as pen
s_color = ['red','yellow','green','blue']

for i in range(4):
    pen.pencolor(s_color[i])
    pen.pensize(i*2+1)
    pen.forward(200)
    pen.right(90)
    