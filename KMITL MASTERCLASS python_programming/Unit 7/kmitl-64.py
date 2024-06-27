import numpy as np
import matplotlib.pyplot as plt
x = [0.5,2,3,4,6,8,9.5]
y = [1,1.3,2.7,5,4,4.5,6]
coefficients = np.polyfit(x,y,6)
polynomial = np.poly1d(coefficients)
xs = np.linspace(0.5,9.5,90)
ys = polynomial(xs)
plt.plot(x,y,'*')
plt.plot(xs,ys)
plt.legend(['n=6'],loc=2)
plt.xlabel('x');plt.ylabel('y')
plt.xlim(0,10);plt.ylim(0,9)
plt.show()
np.polyfit(x,y,n)

