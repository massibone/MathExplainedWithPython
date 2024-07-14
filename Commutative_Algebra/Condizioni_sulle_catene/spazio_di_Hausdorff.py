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
