import matplotlib.pyplot as plt
import numpy as np

x= np.arange(-2*np.pi,2*np.pi,0.1)
y=np.tan(x)
y= 1/(np.cos(x))
z= np.cos(x)
plt.ylim(-3,3)
plt.plot(x,y)
plt.plot(x,z)
#show grid
plt.grid()
plt.show()
