import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi, 0.1)

y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,color='green',label='sin(x)')
plt.plot(x,y2,color='cyan',label='cos')
plt.legend(loc='lower left')
plt.show()
