from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as pl
import numpy as np

fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, np.pi, 100)

# first quarter
phi = np.linspace(0.5*np.pi, 1.0*np.pi, 34)
x = np.outer(np.cos(phi), np.sin(theta))
y = np.outer(np.sin(phi), np.sin(theta))
z = np.outer(np.ones(np.size(phi)), np.cos(theta))
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='c')

# second quarter
phi = np.linspace(1.0*np.pi, 1.5*np.pi, 34)
x = np.outer(np.cos(phi), np.sin(theta))
y = np.outer(np.sin(phi), np.sin(theta))
z = np.outer(np.ones(np.size(phi)), np.cos(theta))
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')

# third quarter
phi = np.linspace(1.5*np.pi, 2.0*np.pi, 34)
x = np.outer(np.cos(phi), np.sin(theta))
y = np.outer(np.sin(phi), np.sin(theta))
z = np.outer(np.ones(np.size(phi)), np.cos(theta))
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='aquamarine')

r = np.linspace(0.,1.,25)
x = np.outer(r, np.sin(theta))
y = 0.*x
z = np.outer(r, np.cos(theta))
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='tomato')

ax.view_init(30.,60.)
pl.show()