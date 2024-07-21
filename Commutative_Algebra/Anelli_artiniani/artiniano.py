import sympy as sp

# Creiamo un anello artiniano usando sympy
# Definiamo il polinomio x^2 + 1 su Z/2Z
A = sp.Poly(x**2 + 1, domain='ZZ') / sp.Ideal(x**2 + 1)

# Verifichiamo se l'anello è artiniano
is_artinian = A.is_artinian

if is_artinian:
    print(f"L'anello A è artiniano.")
else:
    print(f"L'anello A non è artiniano.")
  
