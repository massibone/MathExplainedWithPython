import numpy as np
import matplotlib.pyplot as plt

# Define vertices of equilateral triangle
a = 1
v1 = np.array([0, a])
v2 = np.array([np.sqrt(3)/2*a, -1/2*a])
v3 = np.array([-np.sqrt(3)/2*a, -1/2*a])

# Define centers of circles
c1 = (v1 + v2)/2
c2 = (v2 + v3)/2
c3 = (v3 + v1)/2

# Define radius of circles
r = np.sqrt(3)/2*a

# Define angles for drawing arcs
t = np.linspace(0, 2*np.pi/3, 100)

# Define vertices of Reuleaux triangle
p1 = c1 + r*np.array([np.cos(t), np.sin(t)]).T
p2 = c2 + r*np.array([np.cos(t + 2*np.pi/3), np.sin(t + 2*np.pi/3)]).T
p3 = c3 + r*np.array([np.cos(t + 4*np.pi/3), np.sin(t + 4*np.pi/3)]).T

# Plot Reuleaux triangle
plt.plot(p1[:,0], p1[:,1])
plt.plot(p2[:,0], p2[:,1])
plt.plot(p3[:,0], p3[:,1])
plt.axis('equal')
plt.title('Reuleaux triangle')
plt.show()
