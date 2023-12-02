
def f(x):
    """Definizione della funzione di cui trovare uno zero."""
    return x**3 - 2*x - 5

def bolzano_theorem(a, b, tol=1e-6, max_iter=1000):
    """Applica il teorema di Bolzano per trovare uno zero della funzione in [a, b]."""
    if f(a) * f(b) >= 0:
        print("Il teorema di Bolzano non è applicabile su questo intervallo.")
        return None

    c = a  # Approssimazione iniziale
    iter_count = 0

    while abs(f(c)) > tol and iter_count < max_iter:
        c = (a + b) / 2  # Metodo della bisezione
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return c

# Intervallo iniziale [a, b]
a = 1
b = 3
