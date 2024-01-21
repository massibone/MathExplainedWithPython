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
      
