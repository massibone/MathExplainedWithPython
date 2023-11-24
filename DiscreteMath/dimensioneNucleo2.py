'''
Si consideri l’applicazione lineare f : R
4 → R^2 definita da
f (x; y; z; t) =


x − y + t
2y − z + t
Risolvendo questo sistema di equazioni lineari, possiamo trovare le condizioni necessarie affinché il vettore 
f(x,y,z,t) sia il vettore nullo.
Risultato è f=2
'''

from sympy import symbols, Eq, solve

# Definire le variabili
x, y, z, t = symbols('x y z t')

# Definire l'applicazione lineare f
f_x = x - y + t
f_y = 2*y - z + t

# Risolvere il sistema di equazioni lineari f(x, y, z, t) = 0
sistema_equazioni = [Eq(f_x, 0), Eq(f_y, 0)]
soluzioni = solve(sistema_equazioni, (x, y, z, t))

# Calcolare la dimensione del nucleo
dimensione_nucleo = len(soluzioni)

print(f"Le soluzioni del sistema sono: {soluzioni}")
print(f"La dimensione del nucleo di f è: {dimensione_nucleo}")
