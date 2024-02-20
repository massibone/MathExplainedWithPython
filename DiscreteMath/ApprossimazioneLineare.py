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
# Valore specificato di x intorno al quale vogliamo approssimare il costo totale
x0 = 100

# Calcoliamo il valore esatto di C(x) e della sua approssimazione lineare per x = 100
C_x0 = costo_totale(x0)
C_taylor_x0 = approssimazione_lineare(x0, x0)

# Stampiamo i risultati
print("Valore esatto di C(x) per x = 100:", C_x0)
print("Approssimazione lineare di C(x) per x = 100:", C_taylor_x0)
