'''
Un ideale è come una sottoscatola dentro la tua scatola di mattoncini. Contiene alcuni mattoncini che seguono delle regole particolari. Per esempio, se hai un ideale che contiene tutti i mattoncini rossi, significa che ogni volta che prendi un mattoncino rosso e lo combini con un altro mattoncino, il risultato sarà ancora un mattoncino rosso.

Ideali Primari
Ora, immagina che ci sono delle sottoscatole molto speciali, chiamate ideali primari. Questi ideali hanno una proprietà unica: se hai due mattoncini e il loro prodotto (una costruzione fatta con entrambi) è in questa sottoscatola, allora almeno uno dei mattoncini è quasi sempre in una sottoscatola ancora più speciale chiamata ideale primo.

Intersezione di Ideali Primari
Quando prendi diverse sottoscatole (ideali primari) e guardi quali mattoncini ci sono in comune tra tutte queste sottoscatole, stai facendo un'intersezione di ideali primari. È come trovare tutti i mattoncini che sono presenti in ciascuna delle sottoscatole speciali.
'''
import sympy as sp

# Definiamo l'anello dei polinomi in due variabili x e y
x, y = sp.symbols('x y')
R = sp.PolyRing([x, y], sp.ZZ)

# Definiamo due ideali primari nell'anello
ideal1 = sp.Ideal(x**2, x*y, domain=R)
ideal2 = sp.Ideal(y**2, x*y, domain=R)

# Intersezione di ideali primari
intersection_ideal = ideal1.intersect(ideal2)

# Visualizziamo gli ideali e la loro intersezione
print("Ideale primario 1:", ideal1)
print("Ideale primario 2:", ideal2)
print("Intersezione degli ideali primari:", intersection_ideal)
