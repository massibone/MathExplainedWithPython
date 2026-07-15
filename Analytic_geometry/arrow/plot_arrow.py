import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure(facecolor="Blue")
ax = plt.axes(projection= "3d")
plt.axis("off")
ax.set_facecolor("Cyan")
ax.set_aspect("equal")

#draw the arrow
ax.quiver(0,0,0,1,1,1,length=1.0)

plt.show()