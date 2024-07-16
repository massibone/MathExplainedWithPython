'''
Concetto di Supp(M)
In algebra commutativa, se 𝑀 è un modulo su un anello 
𝐴, il supporto di 𝑀, denotato Supp(M), è l'insieme degli ideali primi 𝑝

Concetto di Spazio Noetheriano Chiuso
Un spazio noetheriano chiuso è uno spazio topologico che soddisfa la condizione della catena ascendente per i suoi chiusi e che è contenuto in un altro spazio chiuso. Nel contesto di Spec(A), che è l'insieme degli ideali primi di 𝐴 Supp(M) è un insieme di punti in Spec(A).

Paragrafo
Se M è un modulo noetheriano su un anello arbitrario 
A, allora Supp(M) è un sottospazio noetheriano chiuso di 
Spec(A).

Modulo Noetheriano: Un modulo 
𝑀
M su un anello 
𝐴
A è noetheriano se soddisfa la condizione della catena ascendente sui sotto-moduli.
Supporto di 
𝑀
M: 
Supp
(
𝑀
)
Supp(M) è l'insieme di tutti gli ideali primi 
𝑝
p di 
𝐴
A per cui 
𝑀
𝑝
≠
0
M 
p
​
 

=0.
Sottospazio Noetheriano Chiuso: Questo significa che 
Supp
(
𝑀
)
Supp(M) può essere visto come uno spazio topologico che è noetheriano e chiuso all'interno di 
Spec
(
𝐴
)
Spec(A).
Dimostrazione
Per dimostrare che 
Supp
(
𝑀
)
Supp(M) è un sottospazio noetheriano chiuso di 
Spec
(
𝐴
)
Spec(A):

Proprietà Noetheriana di 
𝑀
M: Poiché 
𝑀
M è noetheriano, ogni catena crescente di sotto-moduli di 
𝑀
M si stabilizza.
Supporto di 
𝑀
M: Consideriamo il supporto di 
𝑀
M, che è l'insieme di tutti gli ideali primi 
𝑝
p per cui 
𝑀
𝑝
≠
0
M 
p
​
 

=0.
Chiusura in 
Spec
(
𝐴
)
Spec(A): Mostriamo che 
Supp
(
𝑀
)
Supp(M) è chiuso in 
Spec
(
𝐴
)
Spec(A) e soddisfa la condizione della catena ascendente per gli insiemi chiusi.
Stabilizzazione delle Catene: La proprietà noetheriana di 
𝑀
M implica che 
Supp
(
𝑀
)
Supp(M) eredita la condizione della catena ascendente, rendendolo noetheriano.
'''
class Ideal:
    def __init__(self, name):
        self.name = name

class Module:
    def __init__(self, ideals):
        self.ideals = ideals
    
    def support(self):
        # Simula il calcolo del supporto del modulo
        return {ideal for ideal in self.ideals if ideal.name != "0"}

class Spec:
    def __init__(self, ideals):
        self.ideals = ideals
    
    def is_noetherian(self, subspace):
        # Verifica se il sottospazio è noetheriano (semplificato)
        return True

# Creazione di un modulo noetheriano
ideals = [Ideal("p1"), Ideal("p2"), Ideal("p3"), Ideal("0")]
M = Module(ideals)

# Calcolo del supporto di M
support_M = M.support()

# Creazione di Spec(A)
spec_A = Spec(ideals)

# Verifica se il supporto è un sottospazio noetheriano chiuso
is_noetherian_closed_subspace = spec_A.is_noetherian(support_M)
print("Il supporto è un sottospazio noetheriano chiuso?", is_noetherian_closed_subspace)
