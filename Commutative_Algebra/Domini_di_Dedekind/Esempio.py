'''
Problema delle Luci Lampeggianti
Immaginiamo che ci siano tre luci che lampeggiano a intervalli diversi. La prima luce lampeggia ogni 3 secondi, la seconda ogni 4 secondi e la terza ogni 5 secondi. Vogliamo sapere dopo quanti secondi tutte le luci lampeggeranno insieme per la prima volta.

Descrizione del Problema
Abbiamo tre intervalli:

Luce 1: 3 secondi
Luce 2: 4 secondi
Luce 3: 5 secondi

Il problema si riduce a trovare un valore di 
𝑡 che soddisfa tutte le congruenze. Qui, i residui sono tutti zero, quindi possiamo usare il Teorema Cinese dei Resti direttamente.
'''
from sympy.ntheory.modular import crt

# Definizione dei moduli e dei residui
n = [3, 4, 5]
a = [0, 0, 0]

# Utilizzo del Teorema Cinese dei Resti
t, mod = crt(n, a)

print(f"Tutte le luci lampeggeranno insieme ogni {t} secondi.")
