'''Equazioni differenziali parziali'''

import sympy as sp

def d_alembert(eq, x, F):
    # Trova la soluzione generale dell'equazione omogenea associata
    eq_omogenea = eq.subs(F, 0)
    sol_omogenea = sp.dsolve(eq_omogenea)
    
    # Trova una soluzione particolare dell'equazione differenziale
    sol_particolare = sp.dsolve(eq)
    
    # Calcola la soluzione generale
    soluzione_generale = sol_particolare.rhs + sol_omogenea.rhs
    
    return soluzione_generale

# Definizione della variabile indipendente e della funzione incognita
x = sp.symbols('x')
u = sp.Function('u')

# Definizione dell'equazione differenziale e della funzione F(x)
eq = u(x).diff(x, x) + u(x).diff(x) - x
F = 0

# Calcolo della soluzione generale usando il lemma di D'Alembert
soluzione_generale = d_alembert(eq, x, F)
print("La soluzione generale dell'equazione differenziale è:", soluzione_generale)
