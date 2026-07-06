# sin^2 x + cos^2 x = 1 == (sin * x)**2 + (cos * x)**2 = 1
import numpy as np
import math
import matplotlib.pyplot as plt


x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
eq= (y**2 + z**2)
plt.plot(x, y, color='green',label='y=sin(x)')
plt.plot(x, z, color='darkblue',label='cos(x)')
plt.plot(x,eq,color='cyan',label='sin^2x+cos^2x')
plt.legend(loc='lower left')
plt.show()
