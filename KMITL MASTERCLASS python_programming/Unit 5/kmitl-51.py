# Simple math problem

from random import randint

x = randint(1,9)
y = randint(1,9)
z = x + y
print(x,'+',y,'=')
m = int(input("Enter an answer: "))
if(z==m):
    print("Correct")
else:
    print("Wrong")
