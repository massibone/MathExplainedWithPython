'''
Gli anelli graduati sono un concetto fondamentale in algebra commutativa e in geometria algebrica. Un anello graduato è un anello che è diviso in "pezzi" o "livelli" che possono essere studiati separatamente. 
'''

class GraduatedRing:
    def __init__(self):
        self.elements = {}

    def add_element(self, degree, element):
        if degree in self.elements:
            self.elements[degree].append(element)
        else:
            self.elements[degree] = [element]

    def multiply(self, degree1, element1, degree2, element2):
        new_degree = degree1 + degree2
        new_element = f"({element1} * {element2})"
        self.add_element(new_degree, new_element)
        return new_degree, new_element
