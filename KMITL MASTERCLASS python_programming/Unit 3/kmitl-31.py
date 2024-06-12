# Function

def f_x(x):
    y = 3*x**2+1
    return y

for i in range(1, 11, 1):
    print('f(',i,') =', f_x(i))