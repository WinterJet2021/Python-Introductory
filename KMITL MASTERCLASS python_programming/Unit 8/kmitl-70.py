# Drawing an orange square

import turtle as pen
s_color = ['red','yellow','green','blue']

pen.fillcolor('orange')
pen.begin_fill()
for i in range(4):
    pen.pencolor(s_color(i))
    pen.pensize(i*2+1)
    pen.forward(200)
    pen.right(90)
pen.end_fill()