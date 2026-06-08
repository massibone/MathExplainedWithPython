# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Create axis
axes = [5, 5, 5]

# Create Data
data = np.ones(axes, dtype=bool)

# Control Transparency
alpha = 0.9

# Control colour
colors = np.empty(axes + [4], dtype=np.float32)

colors[:] = [1, 0, 0, alpha] # red

# Plot figure
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_facecolor=colors
# Voxels is used to customizations of the
# sizes, positions and colors.
ax.voxels(data, facecolors=colors)
ax.axis('off')
plt.show()
