
import sympy as sp

# Definizione della variabile simbolica
x = sp.symbols('x')

# Espressione da scomporre
espressione = x**4 - 1

# Scomposizione in fattori
fattori = sp.factor(espressione)

print("Scomposizione in fattori:")
print(fattori)
