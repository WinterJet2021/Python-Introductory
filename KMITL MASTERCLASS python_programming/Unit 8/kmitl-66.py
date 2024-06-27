# Fibbocani Number

def fib(num):
    if ((num==0)) or ((num==1)):
        return num
    return(fib(num - 1)) + fib(num - 2)

x = int(input("Input Number:"))
for i in range(x):
    print(fib(i)," ",end=" ")
