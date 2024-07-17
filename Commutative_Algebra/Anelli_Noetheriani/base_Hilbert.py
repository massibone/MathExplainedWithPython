'''
l teorema della base di Hilbert è un risultato fondamentale in algebra commutativa che afferma che se A è un anello noetheriano, allora l'anello dei polinomi A[x] è anch'esso noetheriano. In altre parole, ogni ideale di 
A[x] è finitamente generato.
'''


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __repr__(self):
        return " + ".join(f"{coeff}x^{i}" for i, coeff in enumerate(self.coefficients) if coeff != 0)

class Ideal:
    def __init__(self, generators):
        self.generators = generators
    
    def is_finitely_generated(self):
        # Simula la verifica se l'ideale è finitamente generato
        return len(self.generators) < 10  # Condizione semplificata per l'esempio

class Ring:
    def __init__(self, name):
        self.name = name
        self.ideals = []
    
    def add_ideal(self, ideal):
        self.ideals.append(ideal)
    
    def is_noetherian(self):
        # Verifica se tutti gli ideali sono finitamente generati
        return all(ideal.is_finitely_generated() for ideal in self.ideals)

# Creazione di un anello noetheriano A
A = Ring("A")

# Aggiunta di ideali finitamente generati ad A
A.add_ideal(Ideal([Polynomial([1, 0, 0]), Polynomial([0, 1])]))  # Ideal generato da x^2 e x
A.add_ideal(Ideal([Polynomial([1, 2, 1])]))  # Ideal generato da x^2 + 2x + 1

# Verifica se A è noetheriano
print("L'anello A è noetheriano?", A.is_noetherian())

# Creazione di un anello dei polinomi A[x]
Ax = Ring("A[x]")

# Aggiunta di ideali finitamente generati ad A[x]
Ax.add_ideal(Ideal([Polynomial([1, 0, 0, 0]), Polynomial([0, 1])]))  # Ideal generato da x^3 e x
Ax.add_ideal(Ideal([Polynomial([1, 2, 1, 0])]))  # Ideal generato da x^3 + 2x + 1

# Verifica se A[x] è noetheriano
print("L'anello A[x] è noetheriano?", Ax.is_noetherian())
