def esistenza_minimi(M):
    # Funzione per controllare se un punto è un minimo
    def is_minimo(M, i, j):
        height = M[i][j]
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0 <= x < len(M) and 0 <= y < len(M[0]):
                    if M[x][y] < height:
                        return False
        return True
    
    # Ciclo attraverso ogni punto della superficie
    for i in range(len(M)):
        for j in range(len(M[0])):
            if is_minimo(M, i, j):
                return True  # Se troviamo un minimo, restituiamo True
    
    return False  # Se non troviamo minimi, restituiamo False

# Esempio di utilizzo:
superficie = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if esistenza_minimi(superficie):
    print("La superficie ha minimi.")
else:
    print("La superficie non ha minimi.")
