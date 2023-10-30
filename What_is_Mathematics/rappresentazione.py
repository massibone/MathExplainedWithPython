'''
prende un numero intero inserito dall'utente e lo rappresenta nella forma z
Inserisci un numero intero: 372
z = 300 + 70 + 2

e in base 7
z = 343 + 0 + 28 + 1
'''

def rappresenta_numero(numero):
    # Converti il numero in stringa per lavorare con le singole cifre
    numero_str = str(numero)
    lunghezza_numero = len(numero_str)
    rappresentazione = []

    for i, cifra in enumerate(numero_str):
        # Calcola il termine corrispondente a questa cifra
        termine = int(cifra) * 10 ** (lunghezza_numero - i - 1)
        rappresentazione.append(termine)

    # Unisci la rappresentazione in una stringa
    rappresentazione_str = ' + '.join(map(str, rappresentazione))

    return f"z = {rappresentazione_str}"

# Ottieni l'input dell'utente
numero_intero = int(input("Inserisci un numero intero: "))

# Calcola e stampa la rappresentazione
print(rappresenta_numero(numero_intero))

def rappresenta_in_base7(numero):
    rappresentazione = ''
    if numero == 0:
        rappresentazione = '0'
    else:
        while numero:
            numero, resto = divmod(numero, 7)
            rappresentazione = str(resto) + rappresentazione

    return rappresentazione

# Numero da rappresentare in base 7
numero = int(input("Inserisci un numero intero per sistema base 7: "))

# Calcola la rappresentazione in base 7
rappresentazione_base7 = rappresenta_in_base7(numero)

# Stampa la rappresentazione in base 7
print(f'Rappresentazione di {numero} in base 7: {rappresentazione_base7}')
