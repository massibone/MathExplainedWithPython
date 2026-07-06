
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
#  overwrites matplotlib color cycling and sets all the lines as black
mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
x = np.linspace(-9, 9, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)
a, b, c, d, e, f = 1, -2, 1, 2, 2, -10
def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)


axes()
plt.contour(x, y,(x**2/a**2 - y**2/b**2), [1], colors='k', alpha=.1)
# Eccentricity.
e = np.sqrt(1 + b**2/a**2)
# Foci.
plt.plot(a*e, 0, '.', -a*e, 0, '.')
# Directrices.
plt.axvline(a/e)
plt.axvline(-a/e)
# Asymptotes.
plt.plot(x[0,:], b/a*x[0,:], '--')
plt.plot(x[0,:], -b/a*x[0,:], '--')
plt.show()