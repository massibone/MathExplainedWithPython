import numpy as np

class AbelianTopologicalGroup:
    def __init__(self, elements):
        self.elements = elements

    def add(self, x, y):
        return x + y


    def inverse(self, x):
        return -x

    def is_continuous(self, operation, points, epsilon=1e-5):
        # Verifica se l'operazione è continua in un insieme di punti
        for point in points:
            neighbors = [point + epsilon, point - epsilon]
            results = [operation(point, neighbor) for neighbor in neighbors]
            if not all(np.isclose(results, operation(point, point), atol=epsilon)):
                return False
        return True

# Esempio di gruppo abeliano topologico: i numeri reali
elements = np.linspace(-10, 10, 100)
group = AbelianTopologicalGroup(elements)

# Verifica della continuità dell'operazione di aggiunta
points_to_check = [0, 1, -1, 5, -5]
print("L'operazione di aggiunta è continua?", group.is_continuous(group.add, points_to_check))

# Verifica della continuità dell'operazione di inversione
print("L'operazione di inversione è continua?", group.is_continuous(group.inverse, points_to_check))
