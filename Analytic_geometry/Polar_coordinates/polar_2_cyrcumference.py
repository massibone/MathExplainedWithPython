
import numpy as np

XMIN =-0.15
XMAX = 0.15
YMIN = -0.1
YMAX = 0.1
ZMIN = -0.1
ZMAX = 0.1
sampling = 100

x_ = np.linspace(XMIN, XMAX, sampling)
y_ = np.linspace(YMIN, YMAX, sampling)
z_ = np.linspace(ZMIN, ZMAX, sampling)

x, y, z = np.meshgrid(x_, y_, z_, indexing='ij')



assert np.all(x[:,0,0] == x_)
assert np.all(y[0,:,0] == y_)
assert np.all(z[0,0,:] == z_)

# cylindric coordinates (R, theta, z)
R_coor = []
THETA_coor = []
Z_coor = []

for i in range(sampling-1):
    R = np.sqrt(y[i]**2 + z[i]**2)
    THETA = np.arctan2(y[i],z[i])
    Z = x[i]
    R_coor.append(R)
    THETA_coor.append(THETA)
    Z_coor.append(Z)
