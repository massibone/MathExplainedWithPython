'''
L'approssimazione del costo totale di produzione intorno al livello di produzione 
x=100 utilizzando la formula di Taylor di primo ordine.
'''
# Definiamo la funzione di costo totale
def costo_totale(x):
    return 1000 + 5*x + 0.1*x**2
    
# Definiamo la funzione dell'approssimazione lineare
def approssimazione_lineare(x, x0):
    return 1050 + 5*(x - x0)
