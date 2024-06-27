# Importing from math

import math
print(math.e)

import math
print(math.sqrt(25))

import math
x = int(input("Enter a value for x:"))
y = math.sqrt(x)
print("The root of x is =", y)

f_x = lambda x:x**2+1
a = f_x(4)
print("f_x is =", a)

from random import randint
x = randint(1,9)
print(x)
