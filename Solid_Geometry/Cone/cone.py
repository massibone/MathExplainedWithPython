

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


theta=np.arange(0, 2*np.pi, 0.02)
z_ = np.arange(0,1,0.02)



theta,z_ = np.meshgrid(theta,z_)


z=z_
r= np.sqrt(4 * z)
#equazioni di sistema
x=r*np.cos(theta)
y=r*np.sin(theta)

fig=plt.figure()
ax=Axes3D(fig)

ax.plot_surface(x,y,-z, color="blue", alpha=0.5)
ax.plot_wireframe(x,y,z, color="black", alpha=0.2)



plt.show()