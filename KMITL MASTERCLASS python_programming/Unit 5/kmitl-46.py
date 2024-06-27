import random
A = random.sample(range(1,12),10)
sum_i = 0
for x in A:
    sum_i = sum_i + x
print("A =", A)
print("Sum =", sum_i)

import random 
A = random.sample(range(1,12),10)
m = sum(A)
print("A = :", A)
print("Sum =,", m)

#Function f(x)

def f_x(x):
    m = x**2 + 1
    return m
print("f(x) = x^2 + 1")
print("==============")
for i in range(10):
    print("f(",i,")=",f_x(i))