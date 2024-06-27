# Function and Method

def show(m):
    for i in range(m):
        print("KMITL")

print("Python")
show(3)
print("Science")
show(5)

def add(x,y):
    m = x + y
    return m

a = int(input("Input your first number:"))
b = int(input("Input your second number:"))
print(a, "+", b, "=",add(a,b))

print(add(2,3))
print(add(5,6))


def is_PrimeNumber(n):
    prime = True
    for i in range(2,n):
        if((n%i)==0):
            prime == False
            return prime
    return prime

x = int(input("Input the value you wish to check:"))
print("Value:", x, "is a prime number?:", is_PrimeNumber(x))



