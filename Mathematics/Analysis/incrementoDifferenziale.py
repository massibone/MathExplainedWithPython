'''
upponiamo  di determinare il volume delle pareti di ina scatola cubica chiusa 10x10x10 cm e con pareti di spessore 0,05 cm 
trovare l'incremento della funzione
'''

def volume_scatola_esterna(lato):
    return lato ** 3

def volume_scatola_interna(lato, spessore):
    lato_interno = lato - 2 * spessore
    return lato_interno ** 3

def incremento_volume(lato, spessore):
    return volume_scatola_esterna(lato) - volume_scatola_interna(lato, spessore)

lato = 10  # cm
spessore_pareti = 0.05  # cm

delta_volume = incremento_volume(lato, spessore_pareti)
print(f"L'incremento del volume delle pareti è di {delta_volume} cm³.")
