import numpy as np

class AbelianTopologicalGroup:
    def __init__(self, elements):
        self.elements = elements

    def add(self, x, y):
        return x + y

