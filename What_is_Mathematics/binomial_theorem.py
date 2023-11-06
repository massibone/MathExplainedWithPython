'''
Il teorema del binomio è un importante teorema dell'algebra che espande la potenza di un binomio, ovvero un'espressione del tipo 

(a+b)^n
 , dove a e b sono numeri reali o variabili, e 

n è un numero intero positivo.
'''


import math

def binomial_coefficient(n, k):
    """Calcola il coefficiente binomiale C(n, k)"""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def binomial_theorem(a, b, n):
    """Espandi (a + b)^n utilizzando il teorema del binomio"""
    expansion = []
    for k in range(n + 1):
        term = binomial_coefficient(n, k) * (a ** (n - k)) * (b ** k)
        expansion.append(term)
    return expansion

# Parametri del binomio
a = 3
b = 2
n = 5  # Potenza a cui elevare il binomio

# Espandi il binomio utilizzando il teorema del binomio
expansion = binomial_theorem(a, b, n)

# Stampa l'espansione
print(f"Espansione di ({a} + {b})^{n}:")
for k, term in enumerate(expansion):
    print(f"Termine {k}: {term}")

# Calcola e stampa la somma della espansione
sum_expansion = sum(expansion)
print(f"\nSomma dell'espansione: {sum_expansion}")
