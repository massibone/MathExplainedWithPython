import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create X-Y meshgrid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# create Z data
Z = np.sin(np.sqrt(X**2 + Y**2))

# create a figure and an axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot the surface
ax.plot_surface(X, Y, Z)

# show the plot
plt.show()
