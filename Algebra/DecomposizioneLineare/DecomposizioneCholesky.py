# Creiamo una matrice definita positiva (necessaria per la decomposizione di Cholesky)
A_cholesky = np.array([[4, 2], [2, 3]])

# Decomposizione di Cholesky
L = np.linalg.cholesky(A_cholesky)

print("Matrice triangolare inferiore L:")
print(L)
print("Trasposta di L (L^T):")
print(L.T)
