'''
Questo codice calcola la derivata della funzione radice cubica f(x) = ∛x e la valuta in x = 8.
'''
import sympy as sp

# Definisci la variabile simbolica x
x = sp.Symbol('x')

# Definisci la funzione f(x) = radice terza di x
f = x**(1/3)

# Calcola la derivata di f(x)
f_prime = sp.diff(f, x)

# Valuta la derivata in x = 8
result = f_prime.subs(x, 8)

print("Derivata di f(x) =", f_prime)
print("Derivata valutata in x = 8:", result)
Certamente! Ecco una versione migliorata del codice Python che hai fornito:

python


import sympy as sp

def calcola_derivata_radice_cubica():
    # Definisci la variabile simbolica x
    x = sp.Symbol('x')

    # Definisci la funzione f(x) = radice terza di x
    f = sp.root(x, 3)  # Più preciso di x**(1/3)

    # Calcola la derivata di f(x)
    f_prime = sp.diff(f, x)

    # Semplifica l'espressione della derivata
    f_prime_simplified = sp.simplify(f_prime)

    # Valuta la derivata in x = 8
    x_value = 8
    result = f_prime_simplified.subs(x, x_value)

    # Stampa i risultati
    print(f"Funzione originale: f(x) = {f}")
    print(f"Derivata di f(x): f'(x) = {f_prime_simplified}")
    print(f"Derivata valutata in x = {x_value}: {result}")
    print(f"Risultato numerico approssimato: {float(result)}")

if __name__ == "__main__":
    calcola_derivata_radice_cubica()
