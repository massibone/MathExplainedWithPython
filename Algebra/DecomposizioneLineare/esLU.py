'''
Decomposizione LU: Applicazioni nella simulazione strutturale
In ingegneria civile e meccanica, la decomposizione LU è ampiamente utilizzata per risolvere i sistemi di equazioni che derivano dall'analisi strutturale. Ad esempio, quando si analizza una struttura come un ponte o un edificio, si creano equazioni che descrivono le forze interne in funzione dei carichi esterni. Questo porta a risolvere un sistema di equazioni lineari di grandi dimensioni, che può essere risolto efficientemente usando la decomposizione LU.

Esempio:
Supponiamo di voler risolvere il sistema di equazioni lineari:

𝐴
𝑥
=
𝑏
Ax=b

Dove:

𝐴
A è la matrice dei coefficienti (es. le proprietà della struttura),
𝑏
b è il vettore dei termini noti (es. i carichi esterni),
𝑥
x è il vettore delle incognite (es. le forze interne che vogliamo trovare).
'''
import numpy as np
import scipy.linalg

# Definiamo la matrice dei coefficienti A e il vettore dei termini noti b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Decomposizione LU
P, L, U = scipy.linalg.lu(A)

# Risolviamo il sistema tramite la decomposizione LU
# Risolviamo prima Ly = b
y = np.linalg.solve(L, np.dot(P, b))

# Poi risolviamo Ux = y
x = np.linalg.solve(U, y)

print("Soluzione del sistema x:")
print(x)
