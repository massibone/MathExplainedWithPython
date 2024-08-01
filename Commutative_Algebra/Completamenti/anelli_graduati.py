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


    def display(self):
        for degree in sorted(self.elements.keys()):
            print(f"Degree {degree}: {self.elements[degree]}")

# Creazione di un anello graduato
graduated_ring = GraduatedRing()
graduated_ring.add_element(0, "1")      # elemento neutro
graduated_ring.add_element(1, "x")      # elemento di grado 1
graduated_ring.add_element(2, "x^2")    # elemento di grado 2

# Moltiplicazione di elementi
degree, element = graduated_ring.multiply(1, "x", 1, "x")

# Visualizzazione dell'anello graduato
graduated_ring.display()
