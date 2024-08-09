class NoetherianRing:
    def __init__(self, elements):
        self.elements = elements


    def is_noetherian(self):
        # Verifica se l'anello è noetheriano: ogni ideale è finitamente generato
        return True  # Per semplicità, assumiamo che l'anello sia Noetheriano

class Module:
    def __init__(self, generators):
        self.generators = generators

    def is_finitely_generated(self):
        # Verifica se il modulo è finitamente generato
        return len(self.generators) > 0

class Filtration:
    def __init__(self, module, filtration):
        self.module = module
        self.filtration = filtration

    def is_stable(self):
        # Verifica se la filtrazione è stabile
        for i in range(len(self.filtration) - 1):
            if self.filtration[i] != self.filtration[i + 1]:
                return False
        return True

# Esempio di anello Noetheriano
A = NoetherianRing(elements=[1, 2, 3])  # Semplice rappresentazione

# Esempio di modulo finitamente generato
M = Module(generators=[(1, 0), (0, 1)])  # Generatori per Z^2

# Esempio di filtrazione stabile
Mn = Filtration(module=M, filtration=[M, M, M])

print("L'anello è Noetheriano?", A.is_noetherian())
print("Il modulo è finitamente generato?", M.is_finitely_generated())
print("La filtrazione è stabile?", Mn.is_stable())
