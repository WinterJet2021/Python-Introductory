import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.,5.,0.2)

plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.axis([0,6,0,150])
plt.show()

import matplotlib.pyplot as plt
x = ['Mon','Tue','Wed','Thu','Fri']
y = [10,20,25,30,15]

plt.bar(x,y,color='y',alpha=0.8)
plt.show()

