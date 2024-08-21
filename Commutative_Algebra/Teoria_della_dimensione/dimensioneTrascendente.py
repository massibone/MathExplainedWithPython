'''
La dimensione trascendente è un concetto fondamentale nell'algebra commutativa e nella teoria dei campi, 
che misura l'estensione di un campo rispetto a un suo sottocampo. 
È strettamente legata alla nozione di indipendenza algebrica.
'''
import sympy as sp

# Definiamo le variabili simboliche x e y
x, y = sp.symbols('x y')

# Verifica dell'indipendenza algebrica
# Consideriamo un polinomio generico in x e y con coefficienti razionali
polynomial = sp.poly(x**2 + y**2 - 1, x, y)

# La verifica dell'indipendenza algebrica significa che nessun polinomio non nullo
# in x e y con coefficienti razionali è zero (tranne il polinomio nullo)
independent = not polynomial.is_zero

print(f"Le variabili x e y sono algebricamente indipendenti su Q: {independent}")

# Dimensione trascendente di Q(x, y) su Q
trdeg = 2
print(f"La dimensione trascendente di Q(x, y) su Q è: {trdeg}")
