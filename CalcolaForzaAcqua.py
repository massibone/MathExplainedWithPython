'''
un recipiente a base quadrata di lato a 
e con pareti verticali di altezza h è colmo d'acqua.
Con che forza l'acqua preme su una parete del recipiente?
'''

def calcola_forza(lato_base, altezza_acqua, densita_acqua=1000, accelerazione_gravitazionale=9.8):
    area_parete = lato_base * altezza_acqua
    pressione = densita_acqua * accelerazione_gravitazionale * altezza_acqua
    forza = pressione * area_parete
    return forza

# Parametri del recipiente e dell'acqua
lato_base_recipiente = 1.0  # Lunghezza del lato della base del recipiente
altezza_acqua = 0.5  # Altezza dell'acqua nel recipiente
densita_acqua = 1000  # Densità dell'acqua in kg/m^3
accelerazione_gravitazionale = 9.8  # Accelerazione dovuta alla gravità in m/s^2

# Calcola la forza
forza_esercitata = calcola_forza(lato_base_recipiente, altezza_acqua, densita_acqua, accelerazione_gravitazionale)

# Stampa il risultato
print(f'La forza esercitata dall\'acqua sulla parete del recipiente è di {forza_esercitata:.2f} Newton')

'''
Risultato 2450.00 Newton
Per mettere in prospettiva la forza di 2450 Newton, possiamo confrontarla con forze comuni o situazioni quotidiane. Ecco alcuni esempi di forze che potrebbero essere di dimensioni simili o comparabili:

Peso di un oggetto:

Corrisponde al peso di un oggetto di circa 250 kg (usando 
F=m⋅g, dove 

m è la massa e g è l'accelerazione dovuta alla gravità).
Forza di frenata di un'auto:

La forza di frenata di un'auto può variare, ma potrebbe essere nella gamma di 2000-3000 Newton durante una frenata decisa.
Forza di una persona che spinge:

Una persona in buona forma fisica potrebbe esercitare una forza di spinta di circa 500-1000 Newton.
Forza esercitata da una gru:

Una gru industriale potrebbe esercitare una forza di sollevamento di diverse tonnellate, corrispondente a molte migliaia di Newton.
'''