import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
Se i tre vettori giacciono sullo stesso piano, significa che sono linearmente dipendenti. 
Ma se non giacciono sullo stesso piano, sono linearmente indipendenti.
'''
# Definizione dei vettori (esempio)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

# Creazione della figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origine
ax.quiver(0, 0, 0, 0, 0, 0, color='k')

# Vettori
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', label='v2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', label='v3')

ax.set_xlim([0, max(v1[0], v2[0], v3[0])])
ax.set_ylim([0, max(v1[1], v2[1], v3[1])])
ax.set_zlim([0, max(v1[2], v2[2], v3[2])])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.legend()
plt.show()
