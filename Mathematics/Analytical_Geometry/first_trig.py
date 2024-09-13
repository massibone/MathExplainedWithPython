import numpy as np
import math
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker




xx = np.linspace(-2*np.pi, 2*np.pi,100)
fx = np.cos(xx)**2 + np.sin(xx)** 2

F1 = np.sin(xx)

fig, ax = plt.subplots()

positions = [np.pi / 2 * x for x in range(-4, 5)]
labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', 
                    r'$-\frac{\pi}{2}$', 0, r'$\frac{\pi}{2}$', 
                    r'$+\pi$', r'$\frac{3\pi}{2}$', r'$+2\pi$']
ax.xaxis.set_major_locator(ticker.FixedLocator(positions))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))


ax.plot(xx, F1, xx, fx)

plt.show()