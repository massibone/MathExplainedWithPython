import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import math

G = 4
g = 2
h = 2

a = math.sqrt(math.pow(h,2)+math.pow((((G/2)-(g/2))),2))
Z = np.array([[-1, -1, -1],
                  [(-1+G), -1, -1 ],
                  [(-1+G), (-1+G), -1],
                  [-1, (-1+G), -1],
                  [(-1+(a/3)), (-1+(a/3)), (-1+h)],
                  [(-1+(a/3)+g), (-1+(a/3)), (-1+h)],
                  [(-1+(a/3)+g), (-1+(a/3)+g), (-1+h)],
                  [(-1+(a/3)), (-1+(a/3)+g), (-1+h)]])

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

r = [-1,1]

X, Y = np.meshgrid(r, r)
ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

faces = [[Z[0],Z[1],Z[2],Z[3]],
 [Z[4],Z[5],Z[6],Z[7]],
 [Z[0],Z[1],Z[5],Z[4]],
 [Z[2],Z[3],Z[7],Z[6]],
 [Z[1],Z[2],Z[6],Z[5]],
 [Z[4],Z[7],Z[3],Z[0]],
 [Z[2],Z[3],Z[7],Z[6]]]

ax.add_collection3d(Poly3DCollection(faces,
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

plt.show()