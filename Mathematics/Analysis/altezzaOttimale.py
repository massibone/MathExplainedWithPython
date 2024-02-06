'''
Programma che calcola l'altezza ottimale per posizionare la lampada 
in modo che il bordo della pista di pattinaggio 
riceva la massima illuminazione. 
Supponiamo che la pista sia rappresentata da un segmento 
di retta orizzontale e che la lampada sia posizionata sopra il suo centro.
'''


import math

def altezza_massima_illuminazione(lunghezza_pista, altezza_lampada):
    # Calcoliamo la distanza orizzontale tra la lampada e il bordo della pista
    distanza_orizzontale = lunghezza_pista / 2
    
    # Calcoliamo l'angolo tra la lampada e il bordo della pista
    angolo = math.atan(altezza_lampada / distanza_orizzontale)
    
    # L'altezza massima di illuminazione corrisponde all'altezza della lampada
    # moltiplicata per il seno dell'angolo calcolato
    altezza_massima = altezza_lampada * math.sin(angolo)
    
    return altezza_massima

lunghezza_pista = float(input("Inserisci la lunghezza della pista di pattinaggio: "))
altezza_lampada = float(input("Inserisci l'altezza della lampada: "))

altezza_ottimale = altezza_massima_illuminazione(lunghezza_pista, altezza_lampada)
print(f"L'altezza ottimale per posizionare la lampada affinché il bordo della pista riceva la massima illuminazione è: {altezza_ottimale}")
