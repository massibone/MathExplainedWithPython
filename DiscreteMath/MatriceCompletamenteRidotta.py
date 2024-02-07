'''
Una matrice si dice completamente ridotta secondo la forma di Gauss-Jordan se soddisfa le seguenti condizioni:

Ogni colonna contenente un elemento pivot (il primo elemento non nullo in ogni colonna) deve contenere solo zeri in tutte le posizioni al di fuori del pivot.
Ogni riga contenente un elemento pivot deve contenere solo zeri in tutte le posizioni al di fuori del pivot.
Tutte le righe o colonne nulle devono apparire in basso o a destra della matrice.
Per la matrice A data:
[[ 1  0  0  0]
 [ 0  0 -1  0]
 [ 0  2  0  2]
 [ 0  0  0  0]]
Possiamo vedere che:

La prima colonna contiene un elemento pivot (1) e contiene solo zeri al di fuori del pivot.
La terza colonna contiene un elemento pivot (-1) e contiene solo zeri al di fuori del pivot.
La seconda colonna contiene un elemento pivot (2) e contiene solo zeri al di fuori del pivot.
La quarta colonna è nullo.
Inoltre, tutte le righe nulle appaiono in basso della matrice.

Quindi, la matrice A è completamente ridotta secondo la forma di Gauss-Jordan, con la sequenza di colonne pivot (1,2,3) e la sequenza di righe pivot (1,2,3).

Ricorda che la forma completamente ridotta rappresenta una forma finale di eliminazione gaussiana che semplifica ulteriormente la matrice a scopi di calcoli e analisi.
'''
