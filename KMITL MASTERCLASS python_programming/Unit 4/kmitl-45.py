# More Practice Problems

#5 f(x) = sqrt(x^2 + 3)

import math

def function5(x):
    return math.sqrt(x**2 +3)

# Prompt the user for an input
x = float(input("Enter a value for x: "))

# Calculate the output of each function
y5 = function5(x)

# Print the results
print(f"The range of the function f(x) = sqrt(x^2 + 3) at x = {x} is y = {y5}")

