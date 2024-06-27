# Physics Math Chem Example

sub1 = ['Physics','Math','Chem']
print('My favorite subject is:', sub1)
Data1 = [3,8,2,9,5]
for i in range(5):
    print(Data1[i]) 

sum = 0
for x in range(1,101,1):
               sum = sum + x
               print("sum =", sum)

sum = 0
for x in range (1,101,1):
        if((x%3)==0):
                sum = sum + x
                print("sum =", sum)

sum = 0
for x in range (1,101,1):
        if ((x%3)==0)or((x%5)==0):
                print(x)
                sum = sum + x
                print("sum =", sum)

import random
A = random.sample(range(1,12),10)
sum_i = 0
for x in A:
        sum_i = sum_i + x
        print("A = :",A)
        print("Sum", sum_i)
