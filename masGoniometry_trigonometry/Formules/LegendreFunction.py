import numpy as np
from scipy.special import legendre

x = np.linspace(-1, 1, 1000)

p2 = legendre(2)
p4 = legendre(4)

y2 = p2(x)
y4 = p4(x)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(x, y2, label='n=2')
ax.plot(x, y4, label='n=4')

ax.legend(loc='best')
ax.set_xlabel('x')
ax.set_ylabel('Pn(x)')

plt.show()