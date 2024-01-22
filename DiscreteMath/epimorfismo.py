'''
Per verificare se una funzione 
f:R ^3 →R ^2
  è un epimorfismo, dovremmo verificare se la funzione copre l'intero codominio R^2 . In altre parole, ogni vettore 
w∈R ^2
  deve essere ottenibile come 

f(v) per almeno un vettore v∈R^3

'''

import numpy as np
from scipy.optimize import fsolve

def f(x, y, z):
    return np.array([x + 2*y + z, y + z])

def is_epimorphism(w):
    # Funzione di sistema per risolvere per x, y, z
    def system(vars):
        x, y, z = vars
        return [x + 2*y + z - w[0], y + z - w[1]]
      
  # Soluzione del sistema
    solution = fsolve(system, [0, 0, 0])

    # Verifica se la soluzione è valida
    return np.allclose(f(*solution), w)

# Esempio di vettori w in R^2

w1 = np.array([1, 2])
w2 = np.array([3, 4])

# Verifica se f è un epimorfismo per w1 e w2
print(is_epimorphism(w1))
print(is_epimorphism(w2))
