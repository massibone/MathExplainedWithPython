import matplotlib.pyplot as plt
import math
import numpy as np

def cart2pol(xd_2, yd3):
    xdkw = np.power(xd_2,2)
    yd3kw = np.power(yd3,2)
    rho = np.sqrt(xdkw + yd3kw)
    phi = np.arctan2(yd3kw, xdkw)
    return(rho, phi)


cartesian_coordinates = [(1, 2), (-3, 4), (5, 6)]
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
for x, y in cartesian_coordinates:
    rho, phi = cart2pol(x, y)
    ax.plot(phi, rho)

plt.show()