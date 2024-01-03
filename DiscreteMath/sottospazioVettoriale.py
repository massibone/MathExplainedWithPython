'''
Esempio di sottospazio vettoriale di R^2 potrebbe essere l'insieme S dei vettori 
che appartengono alla retta y=2x
le tre condizioni sono:
1.contenimento dell'origine:Il vettore (0,0) appartiene  a S
2.chiusura rispetto alla somma
3.Chiusura rispetto alla moltiplicazione per uno scalare
'''
import numpy as np

# Verifica della condizione di contenimento dell'origine
origin_belongs_to_S = (0, 0) in [(x, 2*x) for x in np.linspace(-10, 10, 100)]
print("Il vettore zero appartiene a S?", origin_belongs_to_S)

# Verifica della condizione di chiusura rispetto alla somma
v1 = (1, 2)  # Un vettore in S
v2 = (-3, -6)  # Un altro vettore in S
sum_in_S = (v1[0] + v2[0], v1[1] + v2[1]) in [(x, 2*x) for x in np.linspace(-10, 10, 100)]
print("La somma di due vettori in S è in S?", sum_in_S)

# Verifica della condizione di chiusura rispetto alla moltiplicazione per uno scalare
scalar_multiplication_in_S = (2 * v1[0], 2 * v1[1]) in [(x, 2*x) for x in np.linspace(-10, 10, 100)]
print("La moltiplicazione per uno scalare di un vettore in S è in S?", scalar_multiplication_in_S)
