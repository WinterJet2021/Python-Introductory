# Prime Numbers

prime = 0
n = int(input("Enter number: "))
for x in range(2,n):
    if((n%x)==0):
        prime = 1
    if prime == 0:
        print("This is a whole number")
    else:
        print("This is a prime number")
