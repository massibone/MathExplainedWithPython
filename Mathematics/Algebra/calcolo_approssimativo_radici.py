def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Metodo di Newton-Raphson per il calcolo approssimativo delle radici di una funzione.
    
    Args:
    - f: La funzione di cui si desidera trovare la radice.
    - df: La derivata della funzione f.
    - x0: Valore iniziale di x.
    - tol: Tolleranza per il criterio di arresto (default: 1e-6).
    - max_iter: Numero massimo di iterazioni consentite (default: 100).
    
    Returns:
    - radice: Approssimazione della radice della funzione.
    - iterazioni: Numero di iterazioni effettuate.
    """
    x = x0
    iterazioni = 0
    
    while abs(f(x)) > tol and iterazioni < max_iter:
        x = x - f(x) / df(x)
        iterazioni += 1
    
    return x, iterazioni

# Esempio di utilizzo:
def funzione(x):
    return x**2 - 3*x + 2  # Esempio di funzione: f(x) = x^2 - 3x + 2

def derivata_funzione(x):
    return 2*x - 3  # Derivata della funzione: f'(x) = 2x - 3

x0 = 0  # Valore iniziale di x
radice, iterazioni = newton_raphson(funzione, derivata_funzione, x0)

print("Radice approssimata:", radice)
print("Numero di iterazioni:", iterazioni)
