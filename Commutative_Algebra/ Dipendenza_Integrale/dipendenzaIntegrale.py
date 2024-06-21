
-dipendenzaIntegrale.py
import sympy as sp

# Definiamo i simboli per l'algebra commutativa
a0, a1, a2, b = sp.symbols('a0 a1 a2 b')

# Definiamo un'equazione polinomiale che mostra la dipendenza integrale di b da a0, a1, a2
polynomial_eq = b**3 + a2*b**2 + a1*b + a0

# Soluzione dell'equazione polinomiale
solutions = sp.solve(polynomial_eq, b)

# Esempio di numeri interi e numeri razionali
intero = 3
razionale = sp.Rational(3, 4)

# Visualizziamo i risultati
print("Equazione polinomiale che mostra la dipendenza integrale:", polynomial_eq)
print("Soluzioni dell'equazione polinomiale:", solutions)
print("Numero intero:", intero)
print("Numero razionale:", razionale)

