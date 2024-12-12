'''
Decomposizione QR: Applicazioni nella regressione lineare
Nell'analisi statistica e nelle previsioni economiche, 
la regressione lineare viene utilizzata per trovare la relazione tra variabili. 
Durante la risoluzione del problema di minimizzazione dei quadrati 
(es. fitting di una retta ai dati), 
la decomposizione QR è una tecnica efficiente per trovare una soluzione.
'''

# Matrice A che contiene i dati e vettore b con i risultati osservati
A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([1, 2, 2])

# Decomposizione QR
Q, R = np.linalg.qr(A)

# Risolviamo il sistema di equazioni lineari per la regressione
x = np.linalg.solve(R, np.dot(Q.T, b))

print("Coefficiente di regressione (intercetta, pendenza):")
print(x)
