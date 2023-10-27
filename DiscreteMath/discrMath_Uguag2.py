# Inizializza una lista vuota per contenere i valori di x
soluzioni_x = []

# Itera attraverso tutti i possibili valori di x nell'intervallo desiderato
for x in range(-100, 101):  # Esempio: considera x da -100 a 100
    # Calcola le componenti delle due coppie ordinate
    componente1 = (x - 2, x + 1)
    componente2 = (2 * x, 1)
    
    # Confronta le componenti delle coppie ordinate
    if componente1 == componente2:
        soluzioni_x.append(x)

# Stampa i valori di x che soddisfano l'uguaglianza tra le coppie ordinate
print("Valori di x che soddisfano l'uguaglianza tra le coppie ordinate:", soluzioni_x)
