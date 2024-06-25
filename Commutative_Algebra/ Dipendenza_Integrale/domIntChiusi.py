'''
domini di integrità integralmente chiusi in algebra commutativa.
Un dominio di integrità è come una scatola di mattoncini LEGO in cui non puoi mai ottenere un prodotto di due mattoncini che sia zero, a meno che uno dei due mattoncini fosse già zero. Questo significa che puoi fare tutte le costruzioni che vuoi senza che improvvisamente qualcosa si disintegri o diventi inutile.

Un dominio di integrità è integralmente chiuso se ogni volta che prendi un mattoncino che "sembra" fatto dai mattoncini della tua collezione seguendo certe regole, è effettivamente un mattoncino della tua collezione. È come dire che se puoi costruire qualcosa usando i tuoi mattoncini secondo una regola speciale, allora quel qualcosa appartiene davvero alla tua collezione di mattoncini.
'''


import sympy as sp

# Definiamo un anello dei polinomi in una variabile x
R = sp.PolyRing('x', sp.ZZ)
x = R.gens[0]

# Verifichiamo se R è un dominio di integrità
is_integral_domain = R.is_domain

# Definiamo un'elemento y in una estensione di R
y = sp.Symbol('y')
S = sp.PolyRing('x y', sp.ZZ)

# Creiamo un elemento che sembra essere fatto da elementi in R
element_in_S = y**2 - x*y + x**2

# Verifichiamo se l'elemento soddisfa una equazione polinomiale con coefficienti in R
polynomial_eq = y**2 - x*y + x**2
solutions = sp.solve(polynomial_eq, y)

# Verifichiamo se l'elemento appartiene a R
belongs_to_R = all(sol.is_rational_function(x) for sol in solutions)

# Visualizziamo i risultati
print("Anello R:", R)
print("R è un dominio di integrità:", is_integral_domain)
print("Elemento in una estensione di R:", element_in_S)
print("Soluzioni dell'equazione polinomiale:", solutions)
print("L'elemento appartiene a R:", belongs_to_R)
