def viete_formula(a, b, c):
    # Calcolo delle radici
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None  # Radici immaginarie
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root  # Radici coincidenti
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2

def viete_sum_product(a, b, c):
    # Somma e prodotto delle radici usando le formule di Viète
    alpha, beta = viete_formula(a, b, c)
    if alpha is None or beta is None:
        return None, None  # Non è possibile calcolare somma e prodotto
    else:
        sum_of_roots = -b / a
        product_of_roots = c / a
        return sum_of_roots, product_of_roots

# Esempio di utilizzo
a = 1
b = -5
c = 6

sum_of_roots, product_of_roots = viete_sum_product(a, b, c)
print("Somma delle radici:", sum_of_roots)
print("Prodotto delle radici:", product_of_roots)
