import math
print(math.e**2)

import math
x = math.e ** 2
print('the answer is = ', x)

'''sqrt(x)
factorial(x)
pow(x,y)
sin(x)

math.sqrt(100)'''

(6+5) * 3
6 + (5*3)

from random import randint
randint(1,9)
x = randint(1,9)
y = randint(1,9)
z = x + y
print(z)

# How to use Lambdda 
# var = lambda arg1[,arg2]...: expression

f_x = lambda x:x**2+1
a = f_x(4)
print('f_x', a)

ave = lambda x,y,z: (x+y+z)/3
a = ave(4,5,6)
print('f_x =', a)
