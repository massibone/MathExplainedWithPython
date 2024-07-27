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
'''
Il risultato sarà il minimo tempo 𝑡 in cui tutte le luci lampeggiano insieme. In questo caso, il risultato è 60 secondi, poiché 60 è il minimo comune multiplo di 3, 4 e 5.

Utilizzo nella Realtà
In un contesto più reale, il CRT può essere utilizzato in:

Reti di Sensori: Per sincronizzare i tempi di trasmissione dei dati in una rete di sensori che operano a intervalli diversi.
Sistemi Distribuiti: Per pianificare operazioni periodiche in un sistema distribuito dove diverse macchine o processi operano con periodi differenti.
Codici di Temporizzazione: Per creare codici temporali che si ripetono a intervalli regolari e prevedibili, utilizzabili per sincronizzazione in comunicazioni.
''''
