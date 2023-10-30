'''
Se A, B, C, D sono quattro insiemi assegnati,cosa vuol dire (A u B) x (C u D) =(A×(C∪D))∪(B×(C∪D))
esempio
A={1,2}
B={2,3}
C={a,b}
D={b,c}
Calcoliamo il prodotto cartesiano 
(A∪B)×(C∪D):

A∪B, che è l'unione di A e B:
A∪B={1,2,3}

C∪D, che è l'unione di C e D:

C∪D={a,b,c}

(A∪B)×(C∪D)={(1,a),(1,b),(1,c),(2,a),(2,b),(2,c),(3,a),(3,b),(3,c)}


(A×(C∪D))∪(B×(C∪D))={(1,a),(1,b),(1,c),(2,a),(2,b),(2,c),(3,a),(3,b),(3,c)}
'''
from itertools import product

# Definisci gli insiemi A, B, C, D
A = {1, 2}
B = {2, 3}
C = {'a', 'b'}
D = {'b', 'c'}

# Calcola A × (C ∪ D)
product_AC_union_D = set(product(A, C.union(D)))

# Calcola B × (C ∪ D)
product_BC_union_D = set(product(B, C.union(D)))

# Unione tra A × (C ∪ D) e B × (C ∪ D)
result = product_AC_union_D.union(product_BC_union_D)

# Stampa il risultato
print("Risultato:", result)
