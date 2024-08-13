'''
Polinomio di Hilbert
Per moduli graduati su anelli di polinomi, la funzione di Hilbert è spesso un polinomio, 
noto come polinomio di Hilbert. Questo polinomio cattura il comportamento asintotico della funzione di Hilbert.
'''
import sympy as sp

# Definizione del modulo graduato
def hilbert_function(n):
    if n == 0:
        return 1  # Solo il termine costante
    elif n == 1:
        return 1  # Solo il termine lineare
    else:
        return 0  # Non ci sono termini di grado maggiore

# Calcolo dei primi termini della funzione di Hilbert
hilbert_values = [hilbert_function(n) for n in range(5)]
print("Funzione di Hilbert per i primi gradi:", hilbert_values)

# Calcolo del polinomio di Hilbert usando SymPy
n = sp.symbols('n')
hilbert_polynomial = hilbert_values[0] + hilbert_values[1] * n
print("Polinomio di Hilbert:", hilbert_polynomial)
