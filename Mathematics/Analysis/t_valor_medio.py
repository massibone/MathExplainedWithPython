'''
Teorema del valor medio  
es trovare il lim (x - sin x)/x^3 usando tre volte la regola
'''
from sympy import symbols, sin, limit

# Definiamo la variabile simbolica x
x = symbols('x')

# Definiamo l'espressione da valutare
expr = (x - sin(x)) / x**3

# Calcoliamo il limite di expr mentre x tende a 0
lim_expr = limit(expr, x, 0)

print("Il limite di (x - sin(x))/x^3 mentre x tende a 0 è:", lim_expr)
