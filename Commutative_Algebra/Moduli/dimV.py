# Definizione di una funzione per calcolare la dimensione di uno spazio vettoriale
def dimensione_spazio_vettoriale(V):
    return len(V)  # La dimensione è data dal numero di vettori in V

# Creazione di due spazi vettoriali di esempio
spazio_vettoriale_V = [(1, 2), (3, 4), (5, 6)]  # Un insieme di vettori in uno spazio V
spazio_vettoriale_W = [(1, 2), (3, 4)]           # Un altro insieme di vettori in uno spazio W

# Calcolo delle dimensioni dei due spazi vettoriali
dim_V = dimensione_spazio_vettoriale(spazio_vettoriale_V)
dim_W = dimensione_spazio_vettoriale(spazio_vettoriale_W)

# Somma delle dimensioni dei due spazi vettoriali
dim_VW = dim_V + dim_W

# Stampiamo i risultati
print("Dimensione di V:", dim_V)     # Stampiamo la dimensione di V
print("Dimensione di W:", dim_W)     # Stampiamo la dimensione di W
print("Dimensione di V + W:", dim_VW) # Stampiamo la somma delle dimensioni di V e W
