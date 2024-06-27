# Practice Problems

#1. f(x) = x^2 + 2x + 1
#2 f(x) = (x+1)^3 + x
#3 f(x) = root(x+1)
#4 f(x) = 2x + 1

import math

def function1(x):
    return x**2 + 2*x + 1

def function2(x):
    return (x + 1)**3 + x

def function3(x):
    return math.sqrt(x + 1)

def function4(x):
    return 2*x + 1

# Prompt the user for an input
x = float(input("Enter a value for x: "))

# Calculate the output of each function
y1 = function1(x)
y2 = function2(x)
y3 = function3(x)
y4 = function4(x)

# Print the results
print(f"The range of the function f(x) = x^2 + 2x + 1 at x = {x} is y = {y1}")
print(f"The range of the function f(x) = (x + 1)^3 + x at x = {x} is y = {y2}")
print(f"The range of the function f(x) = sqrt(x + 1) at x = {x} is y = {y3}")
print(f"The range of the function f(x) = 2x + 1 at x = {x} is y = {y4}")

