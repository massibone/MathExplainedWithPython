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
        
