def rappresenta_in_base7(numero):
    rappresentazione = ''
    if numero == 0:
        rappresentazione = '0'
    else:
        while numero:
            numero, resto = divmod(numero, 7)
            rappresentazione = str(resto) + rappresentazione

    return rappresentazione

# Calcola le rappresentazioni in base 7 per i primi 6 numeri
rappresentazioni_base7 = [rappresenta_in_base7(i) for i in range(6)]

# Crea la matrice delle somme in base 7 con spazi aggiuntivi tra la terza e la quarta colonna
matrice_somme_base7 = [[rappresenta_in_base7(int(a) + int(b)) if i < 2 else ' ' + rappresenta_in_base7(int(a) + int(b)) for i, a in enumerate(rappresentazioni_base7)] for b in rappresentazioni_base7]
matrice_moltiplicazione_base7 = [[rappresenta_in_base7(int(a) * int(b)) if i < 2 else ' ' + rappresenta_in_base7(int(a) + int(b)) for i, a in enumerate(rappresentazioni_base7)] for b in rappresentazioni_base7]

# Stampa la matrice delle somme in base 7
print("Matrice delle somme dei primi 6 numeri in base 7:")
for riga in matrice_somme_base7:
    print(' '.join(riga))

print("Matrice delle moltiplicazione dei primi 6 numeri in base 7:")
for riga in matrice_moltiplicazione_base7:
    print(' '.join(riga))