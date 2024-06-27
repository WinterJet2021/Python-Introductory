# More customizations (fonts,styling,size)

import turtle as pen
pen.pencolor('blue')
pen.fillcolor('orange')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(100,0)
pen.pendown()
pen.write('hello',move=True,align='left',font=('Arial',24,'bold italic'))