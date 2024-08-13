class PolynomialRing:
    def __init__(self, variables):
        self.variables = variables

    def krull_dimension(self):
        # La dimensione di Krull di un anello di polinomi in n variabili è n
        return len(self.variables)

# Esempio di anello di polinomi
ring1 = PolynomialRing(variables=['x'])
ring2 = PolynomialRing(variables=['x', 'y'])

print(f"La dimensione di Krull di R[x] è: {ring1.krull_dimension()}")
print(f"La dimensione di Krull di R[x, y] è: {ring2.krull_dimension()}")
