import numpy as np
import matplotlib.pyplot as plt
from math import log


a = 2
x = range(1, 100)
y = [log(x1) for x1 in x]
y2 = [log(x2)+2 for x2 in x]
y3 = [log(x3)-3 for x3 in x]
y4 = [-log(x4) for x4 in x]


ax = plt.axes()
plt.plot(x, y, linewidth=1.5, color='b', label=r'y = f(x) ')
plt.plot(x, y2, linewidth=2.5, color='y', label=r'y = f(x)+h h=3 ')
plt.plot(x, y3, linewidth=1.5, color='orange', label=r'y = f(x)-h h=3 ')
plt.plot(x, y4, linewidth=1.5, color='green', label=r'y = -log(x) ')

plt.legend(loc='upper left')
plt.xlabel(r'x')
plt.ylabel(r'y')

plt.show()
plt.clf()
ax.set_ylabel('y-Values')
ax.set_xlabel('x-Values')
ax.set_ylim(0)
ax.set_xlim(0)
plt.plot(x, y, c="b", label="y=log(x) = y=a^x  a>1")
plt.legend()
