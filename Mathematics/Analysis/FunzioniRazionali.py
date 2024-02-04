'''
Un esempio di applicazione dell'integrazione di funzioni razionali si trova nell'analisi di circuiti elettrici. In particolare, consideriamo un circuito RC (resistenza-capacità) in cui abbiamo un condensatore che si carica attraverso una resistenza.
'''
from sympy import symbols, Function, Eq, exp, integrate

# Definiamo le variabili simboliche
t, V0, R, C = symbols('t V0 R C')
V = Function('V')

# Definiamo l'equazione differenziale del circuito RC
equazione_differenziale = Eq(V(t).diff(t), -V(t)/(R*C))

