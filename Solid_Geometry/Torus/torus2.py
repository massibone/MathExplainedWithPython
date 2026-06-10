import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = 2  # major radius of torus
r = 1  # minor radius of torus

u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]
x = (R + r*np.cos(v)) * np.cos(u)
y = (R + r*np.cos(v)) * np.sin(u)
z = r * np.sin(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='plasma')
plt.title('Torus')
plt.show()
