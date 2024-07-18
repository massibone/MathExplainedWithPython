'''
Se 𝐴 è un anello noetheriano e S è una parte moltiplicativa arbitraria di A, allora l'anello localizzato S^(-1) A è anch'esso noetheriano. In altre parole, l'operazione di localizzazione preserva la proprietà noetheriana.
'''
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

    def localize(self, S):
        # Simula la localizzazione del ring con la parte moltiplicativa S
        localized_ideals = [Ideal(ideal.generators) for ideal in self.ideals if set(ideal.generators).isdisjoint(S)]
        localized_ring = Ring(f"S^{-1}{self.name}")
        localized_ring.ideals = localized_ideals
        return localized_ring

# Creazione di un anello noetheriano A
A = Ring("A")

# Aggiunta di ideali finitamente generati ad A
A.add_ideal(Ideal([1, 2, 3]))  # Ideal generato da 1, 2 e 3
A.add_ideal(Ideal([4, 5]))     # Ideal generato da 4 e 5

# Verifica se A è noetheriano
print("L'anello A è noetheriano?", A.is_noetherian())

# Parte moltiplicativa S in A
S = {6, 7}  # Consideriamo una parte moltiplicativa di A

# Localizzazione di A rispetto a S
localized_A = A.localize(S)

# Verifica se S^{-1}A è noetheriano
print("L'anello localizzato S^{-1}A è noetheriano?", localized_A.is_noetherian())
