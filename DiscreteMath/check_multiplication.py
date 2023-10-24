'''
La moltiplicazione di due matrici CxB (con C colonne) non può essere eseguita 
quando il numero di colonne nella prima matrice (C) non è uguale al numero di righe nella seconda matrice (B). In altre parole, la moltiplicazione CxB non è definita se il numero di colonne nella matrice della sinistra (C) non è uguale al numero di righe nella matrice della destra (B).

Per esempio, supponiamo di avere una matrice C di dimensioni 3x4 
(3 righe e 4 colonne) e una matrice B di dimensioni 2x3 (2 righe e 3 colonne). 
La moltiplicazione CxB non è possibile perché il numero di colonne 
nella matrice C (4 colonne) non è uguale al numero di righe nella matrice B 
(2 righe).

'''

def check_multiplication(C, B):
    # C è una matrice con dimensioni m x n
    # B è una matrice con dimensioni p x q
    m, n = len(C), len(C[0])
    p, q = len(B), len(B[0])

    # Verifica se la moltiplicazione è possibile
    if n != p:
        return False
    else:
        return True

# Esempio di utilizzo
C = [[1, 2, 3], [4, 5, 6]]  # Una matrice 2x3
B = [[7, 8], [9, 10], [11, 12]]  # Una matrice 3x2

if check_multiplication(C, B):
    print("La moltiplicazione CxB è possibile.")
else:
    print("La moltiplicazione CxB non è possibile.")
