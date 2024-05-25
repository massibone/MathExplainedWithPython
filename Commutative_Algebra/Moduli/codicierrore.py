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
