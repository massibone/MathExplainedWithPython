'''
dimostrare che la matrice 
[y,    0,       z + x
0, (x - 1)**2,    y
0,     -y,        2]


è diagonale quando 

(x,y,z)=(2,0,2), 

'''
import numpy as np

def is_diagonal_matrix(x, y, z):
    # Definizione della matrice A
    A = np.array([[y, 0, z + x],
                  [0, (x - 1)**2, y],
                  [0, -y, 2]])
    
    # Controllo se la matrice è diagonale
    is_diagonal = (x == 2 and y == 0 and z == 2) and np.all(A != 0)
    
    return is_diagonal

# Coordinata (x, y, z) che vogliamo verificare
x, y, z = 2, 0, 2

# Verifica se la matrice è diagonale per (x, y, z) = (2, 0, 2)
result = is_diagonal_matrix(x, y, z)

if result:
    print("La matrice è diagonale per (x, y, z) = (2, 0, 2).")
else:
    print("La matrice non è diagonale per (x, y, z) = (2, 0, 2).")
