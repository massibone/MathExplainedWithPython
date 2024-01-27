
'''
In economia, l'integrale indefinito può essere utilizzato per calcolare il costo totale, 
il profitto o il surplus del consumatore in determinati modelli economici. 
Ad esempio, quando si analizzano i modelli di domanda e offerta, 
l'integrale indefinito può essere utilizzato per calcolare l'area sotto le curve di domanda e offerta per determinare il surplus del consumatore o del produttore.
Per calcolare il surplus del consumatore, dobbiamo trovare l'area tra la curva di domanda e l'asse delle ordinate sopra il prezzo di equilibrio. 
Per fare ciò, dobbiamo prima trovare il prezzo di equilibrio risolvendo l'equazione di domanda e offerta.
'''
from sympy import symbols, integrate, solve

# Definiamo le variabili simboliche
P = symbols('P')

# Definiamo le equazioni di domanda e offerta
Q_d = 100 - 2*P
Q_s = 50 + P

# Risolviamo l'equazione di domanda e offerta per trovare il prezzo di equilibrio
prezzo_equilibrio = solve(Q_d - Q_s, P)[0]

# Calcoliamo il surplus del consumatore
surplus_consumatore = integrate(Q_d - prezzo_equilibrio, (P, 0, prezzo_equilibrio))

# Stampiamo il risultato
print("Il surplus del consumatore è:", surplus_consumatore)
