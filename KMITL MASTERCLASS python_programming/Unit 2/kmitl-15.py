# SET

A = {1,2,2,3,4,4,5,6,7,7,8,8,8}
print(A)

# Will not repeat multiple numbers of same value

A = {'A,','B','B','C'}
B = {'A','B','C'}
print(A==B)
if 'B' in A:
    print("Yes")

A = {1,2,3,4,5,6,7}
B = {2,4,6,8}
A.add(9)
print("set A = ", A)
print("set B = ", B)
C = A.intersection(B)
print("A ʌ B = ", C)
C = A.union(B)
print("A U B = ", C)
C =A.difference(B)
print("A - B = ", C)
