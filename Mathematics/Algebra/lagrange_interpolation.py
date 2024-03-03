'''
Il contributo di Lagrange all'algebra è significativo e comprende diversi concetti e teoremi importanti. Uno di questi è il Teorema di Lagrange sull'Interpolazione Polinomiale, che afferma che dato un insieme di 
n+1 punti distinti in un piano cartesiano, esiste esattamente un polinomio di grado n o inferiore che passa attraverso tutti questi punti.
'''
from sympy import symbols, simplify

def lagrange_interpolation(points):
    x = symbols('x')
    polynomial = 0
    n = len(points)

    for i in range(n):
        term = points[i][1]
        for j in range(n):
            if j != i:
                term *= (x - points[j][0]) / (points[i][0] - points[j][0])
        polynomial += term

    return simplify(polynomial)
