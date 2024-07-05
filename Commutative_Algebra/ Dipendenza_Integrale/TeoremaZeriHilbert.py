
'''
Il teorema degli zeri di Hilbert (nella sua forma debole) dice che se hai un insieme di equazioni in un campo algebricamente chiuso 
(come i numeri complessi), allora i punti che soddisfano queste equazioni sono esattamente i punti che puoi ottenere dall'ideale generato da queste equazioni.
'''
import sympy as sp

# Definiamo un campo algebricamente chiuso (qui usiamo i numeri complessi)
C = sp.PolyRing('x y', sp.C)

# Definiamo due polinomi
f1 = C.gens[0]**2 + C.gens[1]**2 - 1  # x^2 + y^2 - 1 (un cerchio)
f2 = C.gens[0]**2 - C.gens[1]**2 - 1  # x^2 - y^2 - 1 (iperbole)

# Creiamo un ideale generato da questi polinomi
I = sp.Ideal(f1, f2)

# Troviamo i punti comuni a entrambe le equazioni
solutions = sp.solve_poly_system([f1, f2])

# Visualizziamo i risultati
print("Polinomi f1 e f2:")
print(f1)
print(f2)
print("\nIdeale generato da f1 e f2:", I)
print("Punti comuni alle equazioni (soluzioni):", solutions)
