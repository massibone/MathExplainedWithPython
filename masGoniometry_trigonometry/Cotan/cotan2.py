import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-2*np.pi,2*np.pi, 0.1)

y1=1/np.tan(x)
y2=np.tan(x)

#remove vertical line
y1[:-1][np.diff(y1) > 0] = np.nan
y2[:-1][np.diff(y2) < 0] = np.nan

plt.ylim(-3,3)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
