import numpy as np
from matplotlib.pyplot import*
v = [10,15,20,30,40,50,60,70,80]
s = [5,9,15,18,22,30,35,38,43]
coefficients = np.polyfit(v,s,1)
polynomial = np.poly1d(coefficients)
ys = polynomial(v)
print(coefficients)
print(polynomial)
ys = polynomial(v)
plot(v,s,'o')
show()
