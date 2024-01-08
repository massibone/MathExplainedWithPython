'''
data l' applicazione f. R^3 -> R^3
(x          -->         (2x+3z
y                             3y+z
z)                           2x+2y+z)
come faccio a stabilire che f è iniettiva?
'''

from sympy import symbols, Eq, solve

# Definizione delle variabili
x, y, z = symbols('x y z')

# Definizione dell'equazione
equations = [
    Eq(2*x + 3*z, 0),
    Eq(3*y + z, 0),
    Eq(2*x + 2*y + z, 0)
]

# Risoluzione del sistema di equazioni
solution = solve(equations, (x, y, z))

# Verifica se l'unica soluzione è il vettore nullo
is_injective = all(val == 0 for val in solution.values())

print("L'applicazione è iniettiva:", is_injective)
