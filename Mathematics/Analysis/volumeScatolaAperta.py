'''
con un quadrato di lato a è stata costruita
una scatolas rettangolare aperta di altezza x. il volume V della scatola è V=x(a-2x)^2
'''
def calcola_volume(a, x):
    # Calcolo del volume della scatola rettangolare aperta
    V = x * (a - 2 * x) ** 2
    return V

# Input da parte dell'utente
lato_quadrato = float(input("Inserisci la lunghezza del lato del quadrato (a): "))
altezza_scatola = float(input("Inserisci l'altezza della scatola (x): "))

# Calcola il volume utilizzando la funzione
volume_scatola = calcola_volume(lato_quadrato, altezza_scatola)

# Visualizza il risultato
print(f"Il volume della scatola rettangolare aperta è: {volume_scatola}")
