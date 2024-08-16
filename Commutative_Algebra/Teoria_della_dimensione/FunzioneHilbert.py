import sympy as sp

def funzione_hilbert_univariata(polinomio):
  """
  Calcola la funzione di Hilbert per un polinomio univariato.

  Argomenti:
    polinomio: Un oggetto SymPy che rappresenta un polinomio univariato.

  Restituisce:
    Un dizionario che mappa i gradi ai numeri di Hilbert.
  """
  variabile = sp.symbols('x')
  grado_massimo = sp.degree(polinomio, variabile)
  funzione_hilbert = {}

  for grado in range(grado_massimo + 1):
    coefficienti = sp.Poly(polinomio, variabile, grado).coeffs
    numero_di_monomi = len(coefficienti) - coefficienti.count(0)
    funzione_hilbert[grado] = numero_di_monomi

  return funzione_hilbert

# Esempio di utilizzo
polinomio = sp.Poly('x^3 + 2x^2 - x + 1')
funzione_hilbert = funzione_hilbert_univariata(polinomio)
print(f"La funzione di Hilbert per il polinomio {polinomio} è: {funzione_hilbert}")
