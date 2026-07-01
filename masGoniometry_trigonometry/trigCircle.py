#The equation x**2 + y**2 = 1 describes a circle with radius 1 around the origin
#Due to the trigonometric identity cos(phi)**2 + sin(phi)**2 == 1 this reduces to

#r**2 == 1
#and since r should be real,

#r == 1
#(for any phi).

import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 2*np.pi, 200)
r = 1
x = r*np.cos(phi)
y = r*np.sin(phi)
plt.plot(x,y)
plt.axis("equal")
plt.show()