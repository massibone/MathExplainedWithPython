'''
Un anello di valutazione è come una scatola di mattoncini LEGO in cui puoi ordinare ogni costruzione in base a quanto è grande o piccola. 
C'è una funzione speciale, chiamata valutazione, che ti dice quanto è grande una costruzione rispetto ad altre.

Un Esempio di Anello di Valutazione
Pensa a un numero decimale, come 0.123. La valutazione ti dice quanti numeri ci sono dopo il punto decimale. 
Ad esempio, 0.123 ha una valutazione di 3 perché ci sono tre numeri dopo il punto decimale.
'''

import sympy as sp

# Definiamo un anello dei numeri interi
A = sp.ZZ

# Definiamo una valutazione p-adica per un numero primo p
p = 5

def p_adic_valuation(n, p):
    """Calcola la valutazione p-adica di n rispetto a p."""
    if n == 0:
        return float('inf')
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

# Esempi di numeri interi
numbers = [1, 5, 25, 30, 0]

# Calcoliamo la valutazione p-adica per ogni numero
valuations = {n: p_adic_valuation(n, p) for n in numbers}

# Visualizziamo i risultati
print("Numero primo p:", p)
print("Valutazioni p-adiche dei numeri:", valuations)
