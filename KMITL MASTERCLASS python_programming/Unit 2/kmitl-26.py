# For loop

for x in range(10):
    print(x)

for x in range(1,11):
    print(x," ",end="")

print("Find the sum of range between A-B")
a = int(input("Input a: "))
b = int(input("Input b: "))
sum = 0
for x in range(a,b+1):
    sum = sum + x
print("The sum of range is =", sum)

