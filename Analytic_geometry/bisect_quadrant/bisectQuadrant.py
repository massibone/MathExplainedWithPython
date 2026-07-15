

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-30,30,100)
fig, ax = plt.subplots()
ax.plot(x, x)
ax.plot(x, -(x))
ax.set_aspect('equal')
ax.set(xlim=(-5, 6), ylim=(-4, 6),
       xlabel='x', ylabel='',
       title='y=x blue line     y = -x orange line')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()