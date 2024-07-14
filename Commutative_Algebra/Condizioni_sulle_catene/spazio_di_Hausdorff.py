import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
# Definizione di uno spazio compatto di Hausdorff X
class CompactHausdorffSpace:
    def __init__(self, size):
        self.size = size
        self.figure, self.ax = plt.subplots()
        self.ax.set_xlim(0, size)
        self.ax.set_ylim(0, size)
        self.ax.set_aspect('equal')
def plot_closed_set(self, closed_set, color='r'):
        for (x, y, w, h) in closed_set:
            rect = Rectangle((x, y), w, h, linewidth=1, edgecolor=color, facecolor='none')
            self.ax.add_patch(rect)

    def show(self):
        plt.show()
        
# Definizione delle funzioni continue in C(X)
def create_function(coefs):
    def f(x, y):
        return coefs[0] * x + coefs[1] * y + coefs[2]
    return f

# Definizione della successione strettamente decrescente di chiusi F_n
def create_decreasing_closed_sets(n, size):
    closed_sets = []
    for i in range(n):
        x = y = i * size / (2 * n)
        w = h = size - 2 * x
        closed_sets.append((x, y, w, h))
    return closed_sets
    # Generazione dello spazio e delle funzioni
size = 10
X = CompactHausdorffSpace(size)

# Generazione di funzioni continue
functions = [create_function(np.random.rand(3)) for _ in range(5)]

# Generazione dei chiusi decrescenti
n = 5
closed_sets = create_decreasing_closed_sets(n, size)

# Plot dei chiusi
for i, closed_set in enumerate(closed_sets):
    X.plot_closed_set([closed_set], color=plt.cm.viridis(i / n))

