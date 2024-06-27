# Sets

S = []
for x in range(10):
    S +=[x**2]

print(S)

import matplotlib.pyplot as pl
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,5,9,15,22,29,36,47,62]

pl.title('Problems')
pl.xlabel('Time')
pl.ylabel('Motion (m)')
pl.plot(x,y)
pl.show()

import matplotlib.pyplot as plt

x = range(0,20,2)
y = []

def motion (ux,ax,t):
    S = u*t + (1/2)*a*t**2
    return S

u = int(input("Input the initial speed of car : "))
a = int(input("Input the velocity of car : "))

for t in range(0,20,2):
    S = motion(u,a,t)
    y.append(S)
    print('S(',t,')= ', S)

plt.title("Motion")
plt.ylabel("S")
plt.xlabel("t")
plt.plot(x,y)
plt.show()
