'''
Il gruppo di Grothendieck, denotato spesso come 
K 0 o K(X), è una costruzione matematica che consente di assegnare a ogni spazio topologico o anello una sorta di "conteggio" o "classificazione" delle sue caratteristiche principali.

Nel contesto degli anelli o degli spazi topologici, il gruppo di Grothendieck tiene traccia di oggetti come:

Moduli: rappresentazioni di spazi con regole specifiche.
Fasce di coomologia: misure di come le parti di uno spazio sono connesse tra loro.
Dimensioni: misure di quanto grande o complicato è uno spazio.
'''

# Esempio di conteggio degli elementi in una lista
from collections import Counter

# Lista di mattoncini Lego di diversi tipi
lego_bricks = ['rosso', 'blu', 'verde', 'rosso', 'giallo', 'blu', 'verde']

# Conteggio delle occorrenze di ciascun tipo di mattoncino
brick_counts = Counter(lego_bricks)

# Stampare il conteggio
for brick, count in brick_counts.items():
    print(f"{brick}: {count} mattoncini")

# Questo esempio mostra come si potrebbe "contare" i diversi tipi di mattoncini Lego
# analogamente a come il gruppo di Grothendieck tiene traccia delle proprietà degli spazi.
