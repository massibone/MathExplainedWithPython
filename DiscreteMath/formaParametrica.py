'''
La forma parametrica di un sistema di equazioni lineari implica 
esprimere le variabili in funzione di uno o più parametri. 
Nel tuo caso, la forma parametrica è fornita da:

x1= -3 - 7t;
x2= 3 - t;
x3= 7t - 5; 
x4= 8t
Quando sostituisci questi valori nell'equazione originale, dovresti ottenere una soluzione soddisfacente. 
Ad esempio, prendiamo la prima equazione

2x1 − x2 + 6x4 = 2
Sostituendo i valori parametrici otteniamo:

2(-3-7t) - (3-t)+6(8t)=2

'''

import sympy as sp

# Definisci le variabili e il parametro t
t = sp.symbols('t')
x1, x2, x3, x4 = -3 - 7*t, 3 - t, 7*t - 5, 8*t

# Definisci le equazioni del sistema
eq1 = 2*x1 - x2 + 6*x4 - 2
eq2 = x1 + 2*x2 - x3 + 2*x4 - 1
eq3 = x2 - 2*x3 + x4 - 1

# Risolvi le equazioni per t
sol_t = sp.solve([eq1, eq2, eq3], t)

# Verifica se la soluzione è valida per i valori di t trovati
sol_valida = [(x1.subs(t, sol), x2.subs(t, sol), x3.subs(t, sol), x4.subs(t, sol)) for sol in sol_t]

# Stampa i risultati
print("Valori di t che rendono la soluzione valida:", sol_t)
print("Soluzioni valide per i valori di t trovati:", sol_valida)
