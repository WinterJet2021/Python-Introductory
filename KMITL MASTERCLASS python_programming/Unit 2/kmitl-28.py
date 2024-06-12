# Continue from previous kmitl-27.py

import random
A = random.sample(range(1, 12), 10)
total_sum = sum(A)
print("A =", A)
print("Sum =", total_sum)

import random
A = random.sample(range(1, 12), 10)
a = int(input("Input a: "))
b = int(input("Input b: "))
for x in range(a,b+1):
        sum = a + b
        if ((sum%3)==0)or((sum%5)==0):
                print(sum)
                sum = sum + x   
                print("sum =", sum)

            