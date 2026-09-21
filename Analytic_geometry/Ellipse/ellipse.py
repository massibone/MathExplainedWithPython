from matplotlib.patches import Ellipse
from matplotlib import pyplot as plt

plt.axes()
ax = plt.gca()

ellipse = Ellipse(xy=(157.18, 68.4705), width=0.036, height=0.012, 
                        edgecolor='c', fc='None', lw=2)
ax.add_patch(ellipse)
#plt.grid(True)
plt.axis('scaled')
plt.show()