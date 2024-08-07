# Matrix Addition

A = [[2,2,1],[3,2,1],[4,1,2]]
B = [[3,2,1],[2,1,0],[1,2,3]]
C = [[0,0,0],[0,0,0],[0,0,0]]

print('-----------------------------------------------------------------------------------------------')

for y in range(3):
    for x in range(3):
        C[y][x]=A[y][x]+B[y][x]

print(C)

print('-----------------------------------------------------------------------------------------------')

A = [[2,2,1],[3,2,1],[4,1,2]]
B = [[3,2,1],[2,1,0],[1,2,3]]
C = [[0,0,0],[0,0,0],[0,0,0]]

def add_matrix(m,n):
    for y in range(3):
        for x in range(3):
            C[y][x]=A[y][x]+B[y][x]

def show_matrix(M):
    for y in M:
        for x in y:
            print(x,'',end='')
        print()

add_matrix(A,B)
show_matrix(C)

print('-----------------------------------------------------------------------------------------------')

import numpy as np
A = np.array([[2,2,1],[3,2,1],[4,1,2]])
B = np.array([[3,2,1],[2,1,0],[1,2,3]])
C = A + B
print(C)

print('-----------------------------------------------------------------------------------------------')
