'''
 Se f(x) è un polinomio a coefficienti in un campo (come i numeri reali o complessi), allora ogni radice del polinomio 
f(x) corrisponde a un fattore lineare di f(x).
'''

import sympy as sp

# Definiamo il simbolo x
x = sp.symbols('x')

# Definiamo il polinomio
polynomial = x**2 - 5*x + 6

# Troviamo le radici del polinomio
roots = sp.solve(polynomial, x)

# Fattorizziamo il polinomio
factored_polynomial = sp.factor(polynomial)

# Stampiamo le radici e la fattorizzazione
print(f"Radici del polinomio {polynomial}:")
for root in roots:
    print(f"x = {root}")

print(f"\nFattorizzazione del polinomio {polynomial}:")
print(factored_polynomial)

