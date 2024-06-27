import matplotlib.pyplot as pl
pl.axis([0,10,0,10])
pl.plot(5,5,'x')
pl.show()

for x in range(10):
    y = x
    pl.plot(x,y,'x')
pl.show()

x = range(0,16,2)
y = [25,45,60,15,23,89,12,20]
pl.plot(x,y)
pl.show()



