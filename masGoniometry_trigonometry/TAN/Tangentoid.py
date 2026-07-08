The tangentoid is the plot of the tangent function.

If the plane of the tangentoid is winded into a cylinder

of revolution with directrix Oy and radius b/2, 

then we get a horopter curve.  

'''

import matplotlib.pyplot as plt

import numpy as np

x= np.arange(-2*np.pi,2*np.pi,0.1)

y=np.tan(x)

y[:-1][np.diff(y) < 0] = np.nan

plt.ylim(-3,3)

plt.plot(x,y)

#show grid

plt.grid()

plt.show()
