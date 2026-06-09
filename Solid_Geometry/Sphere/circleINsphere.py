## plot a circle on the sphere using spherical coordinate.
import numpy as np
import matplotlib.pyplot as plt

# a complete sphere
R = 10
theta = np.linspace(0, 2 * np.pi, 1000)
phi = np.linspace(0, np.pi, 1000)
x_sphere = R * np.outer(np.cos(theta), np.sin(phi))
y_sphere = R * np.outer(np.sin(theta), np.sin(phi))
z_sphere = R * np.outer(np.ones(np.size(theta)), np.cos(phi))

# a complete circle on the sphere
x_circle = R * np.sin(theta)
y_circle = R * np.cos(theta)

# 3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='blue', alpha=0.2)
ax.plot(x_circle, y_circle, 0, color='green')
plt.show()
