import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc

LW = 2
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.axis('off')

ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)


# Draw the axes
x = 0
y = 2
dx = 5
dy = 0
xhat = FancyArrowPatch((x, y), (x+dx, y+dy), arrowstyle='->', mutation_scale=10, linewidth=LW, color='k')
ax.add_patch(xhat)
plt.text(x+dx/2.0-0.5, y+dy/2.0-0.5, 'x')

dx = 0
dy = 5
yhat = FancyArrowPatch((x, y), (x+dx, y+dy), arrowstyle='->', mutation_scale=10, linewidth=LW, color='k')
ax.add_patch(yhat)
plt.text(x+dx/2.0-0.5, y+dy/2.0-0.5, 'y')
plt.show()
