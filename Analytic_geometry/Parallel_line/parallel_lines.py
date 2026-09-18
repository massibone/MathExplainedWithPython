import matplotlib.pyplot as plt
import math
import numpy as np

x=[0, 7]
y=[5, 2]
plt.plot(x,y)

o = np.subtract(2, 5)  # y[1] - y[0]
q = np.subtract(7, 0)  # x[1] - x[0]
slope = o/q

#(m,p) are the new coordinates to plot the parallel line
m = 3
p = 2

axes = plt.gca()
x_val = np.array(axes.get_xlim())
y_val = np.array(slope*(x_val - m) + p)
plt.plot(x_val,y_val, color="red", linestyle="--")
plt.show()