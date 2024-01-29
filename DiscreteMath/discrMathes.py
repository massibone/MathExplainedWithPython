'''
Siano A, B e C tre matrici.Quale
delle seguenti condizioni devono soddisfare gli interi m, n, p, q, r, s, affinché la matrice
data da A+B^t- C sia definita?

Le matrici A e C devono avere lo stesso numero di righe e lo stesso numero di colonne
B deve avere un numero di colonne uguale al numero di righe di 
A e C 
affinché la trasposizione B^T
  sia definita.
m (righe di A) deve essere uguale a m (righe di C)
n (colonne di A) deve essere uguale a n (righe di B)
p (righe di B) deve essere uguale a n (colonne di C)

'''
import numpy as np

def is_matrix_defined(A, B, C):
    m_A, n_A = A.shape
    m_B, n_B = B.shape
    m_C, n_C = C.shape

    # Verifica delle condizioni
    return m_A == m_C and n_A == n_B and m_B == n_C

# Dimensioni delle matrici
m, n, p = 3, 2, 3  # Esempio di dimensioni
r, q, s = 3, 2, 3  # Esempio di dimensioni

# Creazione di matrici casuali con le dimensioni specificate
A = np.random.rand(m, n)
B = np.random.rand(n, p)
C = np.random.rand(r, q)

# Calcolo della matrice risultante A + B^T - C
result_matrix = A + B.T - C

# Verifica se la matrice risultante è definita
is_defined = is_matrix_defined(A, B, C)

print("Matrice risultante A + B^T - C:")
print(result_matrix)

if is_defined:
    print("La matrice risultante è definita.")
else:
    print("La matrice risultante non è definita.")
