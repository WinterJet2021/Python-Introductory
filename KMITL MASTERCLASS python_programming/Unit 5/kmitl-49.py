# Quadratic Factoring

import math
A = int(input("A = :",))
B = int(input("B = :",))
C = int(input("C = :",))
x1 = (-B+math.sqrt((B**2)-4*A*C))/(2*A)
x2 = (-B-math.sqrt((B**2)-4*A*C))/(2*A)
print("The roots are:", x1, "and", x2)

