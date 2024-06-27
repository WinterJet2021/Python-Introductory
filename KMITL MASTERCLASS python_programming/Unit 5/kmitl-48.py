import math
a= int(input("a =:"))
b = int(input("b =:"))
c = int(input("c =:"))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area = %6.2f"%area)

#Basic Physics Problem
# S = ut+(1/2)at^2

u = 2
a = 3
def motion(t):
    s = u*t+0.5*a*(t**2)
    return s

for x in range(2,21,2):
    print("t =", "s =", motion(x))