'''
dato W = ⟨v 1 = (1; 5; −1); v 2 = (2; 0; 1); v 3 = (1; 1; 3); v 4 = (−1; 1; 0)⟩: quali sono le possibili basi di W?
Per determinare le possibili basi dello spazio vettoriale W generato da {v1, v2, v3, v4}, dobbiamo prima assicurarci che questi vettori siano linearmente indipendenti. Una volta stabilita la linearità indipendenza, possiamo selezionare un sottoinsieme di vettori di W per formare una base.

Per verificare la linearità indipendenza, possiamo creare una matrice utilizzando i vettori dati come colonne e cercare il rango della matrice. Se il rango della matrice è uguale al numero di vettori (nel nostro caso, 4), allora i vettori sono linearmente indipendenti.
Se i vettori sono linearmente indipendenti, allora qualsiasi sottoinsieme di 3 vettori sarà una base di W. Poiché ci sono 4 vettori, ci sono diverse combinazioni possibili per selezionare una base di 3 vettori da {v1, v2, v3, v4}. Ad esempio, una possibile base potrebbe essere {v1, v2, v3}, un'altra potrebbe essere {v1, v2, v4}, e così via.

'''
import numpy as np

# Definisci i vettori
v1 = np.array([1, 5, -1])
v2 = np.array([2, 0, 1])
v3 = np.array([1, 1, 3])
v4 = np.array([-1, 1, 0])

# Crea la matrice con i vettori come colonne
A = np.column_stack((v1, v2, v3, v4))

# Calcola il rango della matrice
rank_A = np.linalg.matrix_rank(A)

if rank_A == 4:
    print("I vettori sono linearmente indipendenti.")
else:
    print("I vettori sono linearmente dipendenti.")
