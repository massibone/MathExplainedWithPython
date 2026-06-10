mport numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(facecolor="Blue")
ax = plt.axes(projection= "3d")
plt.axis("off")
ax.set_facecolor("Cyan")

p = np.linspace(0, 2*np.pi, 20)
c,a= 1, 0.4
U, V = np.meshgrid(p, p)
X = (c+a*np.cos(V))*np.cos(U)
Y = (c+a*np.cos(V))*np.sin(U)
Z = a*np.sin(V)

ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)

ax.plot_surface(X, Y, Z, rstride=1,cstride=1,color ='Orange')
plt.show()

