'''
come si trasforma in frazione ordinaria la frazione periodica mista alfa=0,13555...., considerandola come limite della corrispondente frazione finita?
la parte intera e la parte frazionaria periodica. Ad esempio, se hai α = 0,13555..., scriveresti α come α = 0 + 0,13555....
α = 0,13555... = 0 + 0,13555... = 0 + 0,13555... = 0 + 13/100 + 555/10000
α = 130555 / 1000000 = 661/5000
'''

def frazione_periodica_mista_to_frazione_ordinaria(parte_intera, parte_periodica):
    parte_intera = int(parte_intera)
    parte_periodica = parte_periodica.rstrip('0')  # Rimuovi zeri finali dalla parte periodica
    parte_periodica_int = int(parte_periodica)
    
    lunghezza_periodo = len(parte_periodica)
    denominatore = 10 ** lunghezza_periodo - 1
    
    numeratore = parte_intera * denominatore + parte_periodica_int
    frazione_ordinaria = numeratore / denominatore
    
    return frazione_ordinaria

parte_intera = 0
parte_periodica = "13555"  # Inserisci la parte periodica qui

frazione_ordinaria = frazione_periodica_mista_to_frazione_ordinaria(parte_intera, parte_periodica)
print("Frazione ordinaria:", frazione_ordinaria)
