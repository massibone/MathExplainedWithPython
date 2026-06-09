from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(facecolor="Cyan")
ax = plt.axes(projection= "3d")
plt.axis("off")
ax.set_facecolor("Cyan")
# draw sphere
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
# alpha controls opacity
ax.plot_surface(x, y, z, color="g", alpha=0.3)

# a random array of 3D coordinates in [-1,1]
bvecs= np.random.randn(20,3)

# tails of the arrows
tails= np.zeros(len(bvecs))

# heads of the arrows with adjusted arrow head length
ax.quiver(tails,tails,tails,bvecs[:,0], bvecs[:,1], bvecs[:,2],
          length=1.0, normalize=True, color='r', arrow_length_ratio=0.15)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.set_title('vectors inside sphere')

plt.show()
