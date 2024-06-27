# Data and Statistics

a = [1,12,5,17,21,8,25,30,16,9]
print("The number of the members are",len(a))
print("Members are",a)
print("The highest value for a member is",max(a))
a.sort()
print("The numbered members in ordered list is presented",a)

print("---------------------------------------------------------------------------------------------------")

import random
A = []
for i in range(10):
    A+=[random.randint(10,99)]
print(A)
print("The highest number is",max(A))
print("The amount of numbers is",len(A))
A.sort()
print("The numbers in ordered list is presented")
print(A)

print("---------------------------------------------------------------------------------------------------")

m = []
for i in range(10):
    x = int(input("Enter a number:"))
    m.append(x)
print(m)


