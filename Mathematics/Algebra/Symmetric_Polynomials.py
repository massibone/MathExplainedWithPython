'''
Il teorema dei polinomi simmetrici afferma che ogni polinomio può essere espresso come combinazione di polinomi simmetrici nelle sue radici. Questi polinomi simmetrici possono essere ottenuti dalle potenze simmetriche delle radici.
'''
from sympy import symbols, symprod

# Definizione dei simboli
x, a, b, c = symbols('x a b c')

# Polinomio di secondo grado
polynomial = a*x**2 + b*x + c

# Calcolo delle radici del polinomio
roots = symprod(x - root for root in polynomial.roots())

# Polinomi simmetrici
symmetric_polynomials = [roots, -b/a, c/a]

# Stampare i polinomi simmetrici
print("Symmetric Polynomials:")
for i, p in enumerate(symmetric_polynomials):
    print(f"Polynomial {i+1}: {p}")
