'''
Un esempio di applicazione dell'integrazione di funzioni razionali si trova nell'analisi di circuiti elettrici. In particolare, consideriamo un circuito RC (resistenza-capacità) in cui abbiamo un condensatore che si carica attraverso una resistenza.
'''
from sympy import symbols, Function, Eq, exp, integrate

# Definiamo le variabili simboliche
t, V0, R, C = symbols('t V0 R C')
V = Function('V')

# Definiamo l'equazione differenziale del circuito RC
equazione_differenziale = Eq(V(t).diff(t), -V(t)/(R*C))

# Risolviamo l'equazione differenziale
soluzione = Eq(V(t), integrate(equazione_differenziale.rhs, t) + C1)

# Applichiamo la condizione iniziale V(0) = V0
soluzione_con_condizione_iniziale = soluzione.subs({V(0): V0})

# Risolviamo per la costante C1
C1_espressa_in_funzione_di_V0 = solve(soluzione_con_condizione_iniziale, 'C1')[0]

# Sostituiamo la costante C1 nella soluzione generale
soluzione_finale = soluzione.subs({'C1': C1_espressa_in_funzione_di_V0})

# Stampiamo la soluzione finale
print("L'equazione della tensione sul condensatore nel tempo è:")
print(soluzione_finale)
