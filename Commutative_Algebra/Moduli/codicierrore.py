'''
 codice di correzione degli errori basato su moduli. Il codice utilizza bit di parità per rilevare e correggere errori nella trasmissione di un messaggio.
'''

import random

def encode_message(message, n, k):
    """
    Codifica un messaggio aggiungendo i bit di parità.
    
    Args:
        message (str): Il messaggio da codificare.
        n (int): Il numero totale di bit nella parola di codice.
        k (int): Il numero di bit di dati (senza bit di parità).
    
    Returns:
        str: La parola di codice generata con bit di parità.
    """
    # Inizializza la parola di codice con tutti 0
    encoded_message = [0] * n
    
    # Copia i bit di dati nel messaggio codificato
    for i in range(k):
        encoded_message[2**i - 1] = int(message[i])
    
# Calcola i bit di parità
    for i in range(k):
        parity_bit_index = 2**i - 1
        for j in range(2**i, n, 2**(i+1)):
            for l in range(j, min(j + 2**i, n)):
                encoded_message[parity_bit_index] ^= encoded_message[l]
    
    return ''.join(map(str, encoded_message))

def introduce_error(encoded_message):
    """
    Introduce un errore casuale nella parola di codice.
    
    Args:
        encoded_message (str): La parola di codice da modificare.
    
    Returns:
        str: La parola di codice con un bit di errore.
    """
    index = random.randint(0, len(encoded_message) - 1)
    # Inverti il bit all'indice selezionato per introdurre l'errore
    encoded_message = list(encoded_message)
    encoded_message[index] = '1' if encoded_message[index] == '0' else '0'
    return ''.join(encoded_message)

def decode_message(encoded_message, n, k):
    """
    Decodifica una parola di codice corrotta e corregge eventuali errori.
    
    Args:
        encoded_message (str): La parola di codice corrotta.
        n (int): Il numero totale di bit nella parola di codice.
        k (int): Il numero di bit di dati (senza bit di parità).
    
    Returns:
        str: Il messaggio originale, corretto se necessario.
    """
    decoded_message = []
    # Calcola i bit di parità e controlla se ci sono errori
    for i in range(k):
        parity_bit_index = 2**i - 1
        parity = 0
        for j in range(parity_bit_index, n, 2**(i+1)):
            for l in range(j, min(j + 2**i, n)):
                parity ^= int(encoded_message[l])
        # Verifica se c'è un errore nei bit di parità
        if parity != int(encoded_message[parity_bit_index]):
            print("Errore rilevato nel bit di parità", i+1)
            # Correggi il bit errato
            encoded_message = list(encoded_message)
            encoded_message[parity_bit_index] = str(parity)
            encoded_message = ''.join(encoded_message)
    
    # Rimuovi i bit di parità dalla parola di codice
    for i in range(n):
        if i + 1 not in [2**j - 1 for j in range(k)]:
            decoded_message.append(encoded_message[i])
    
    return ''.join(decoded_message)

# Parametri del codice di correzione degli errori
n = 7  # Numero totale di bit nella parola di codice
k = 3  # Numero di bit di dati (senza bit di parità)

# Messaggio originale
message = "101"

# Codifica il messaggio aggiungendo i bit di parità
encoded_message = encode_message(message, n, k)
print("Messaggio codificato:", encoded_message)

# Introduce un errore casuale nella parola di codice
corrupted_message = introduce_error(encoded_message)
print("Messaggio corrotto:", corrupted_message)

# Decodifica il messaggio corrotto e corregge eventuali errori
decoded_message = decode_message(corrupted_message, n, k)
print("Messaggio decodificato:", decoded_message)
