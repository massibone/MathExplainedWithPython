'''
Un spazio noetheriano è uno spazio topologico dove ogni sottoinsieme chiuso può essere rappresentato come un'unione finita di sottospazi chiusi irriducibili. Questo significa che ogni chiuso può essere scomposto in un numero limitato di parti che non possono essere ulteriormente scomposte.
'''
class Subspace:
    def __init__(self, name, is_irreducible=False):
        self.name = name
        self.is_irreducible = is_irreducible

class Space:
    def __init__(self):
        self.subspaces = []

    def add_subspace(self, subspace):
        self.subspaces.append(subspace)

    def is_noetherian(self):
        for subspace in self.subspaces:
            if not subspace.is_irreducible and not self.can_be_decomposed(subspace):
                return False
        return True

    def can_be_decomposed(self, subspace):
        # Verifica se il sottospazio può essere decomposto in unione finita di sottospazi irriducibili
        # Simulazione semplice per l'esempio
        return any(s.is_irreducible for s in self.subspaces)

# Creazione di uno spazio noetheriano
space = Space()

# Aggiunta di sottospazi irriducibili
space.add_subspace(Subspace("Subspace1", is_irreducible=True))
space.add_subspace(Subspace("Subspace2", is_irreducible=True))
space.add_subspace(Subspace("Subspace3", is_irreducible=True))

# Aggiunta di un sottospazio non irriducibile
space.add_subspace(Subspace("Subspace4", is_irreducible=False))

# Verifica se lo spazio è noetheriano
print("Lo spazio è noetheriano?", space.is_noetherian())
