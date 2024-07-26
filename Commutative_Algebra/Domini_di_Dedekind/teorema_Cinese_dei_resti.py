from sympy import symbols, Eq, solve
from sympy.ntheory.modular import crt

# Definizione dei moduli e dei residui
n = [3, 4, 5]
a = [2, 3, 1]

# Utilizzo del Teorema Cinese dei Resti
x, mod = crt(n, a)

print(f"Il valore di x che soddisfa tutte le congruenze è: {x} modulo {mod}")

