'''
Il principio del minimo intero stabilisce che qualsiasi insieme non vuoto 
di numeri interi positivi deve avere un elemento minimo, 
cioè un numero intero nell'insieme che è minore o uguale a 
qualsiasi altro numero intero nell'insieme.

'''

def minimo_intero(insieme):
    if not insieme:
        return None  # Restituisce None se l'insieme è vuoto
    minimo = float('inf')  # Imposta il minimo a infinito inizialmente
    for numero in insieme:
        if numero < minimo:
            minimo = numero
    return minimo

# Esempio di utilizzo
insieme_numeri = [5, 2, 8, 1, 10]
minimo = minimo_intero(insieme_numeri)

print("L'insieme è:", insieme_numeri)
print("Il minimo intero dell'insieme è:", minimo)
