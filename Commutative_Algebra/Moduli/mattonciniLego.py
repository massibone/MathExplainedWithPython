'''
Supponiamo di avere i seguenti tipi di mattoncini LEGO disponibili:

Tipo A: Mattoncino rosso rettangolare
Tipo B: Mattoncino blu rettangolare
Tipo C: Mattoncino verde rettangolare
# Definizione dei vettori che rappresentano i mattoncini LEGO
v_A = (3, 0, 2)  # Vettore per i mattoncini di tipo A (rosso)
v_B = (1, 2, 1)  # Vettore per i mattoncini di tipo B (blu)
'''

# Creazione del modulo finitamente generato usando i vettori dei mattoncini
modulo_generato = [v_A, v_B]

# Stampiamo il modulo finitamente generato e alcune combinazioni lineari
print("Modulo finitamente generato:")
for v in modulo_generato:
    print("Mattoncini:", v)

# Esempio di combinazione lineare
combinazione_lineare = (2 * v_A[0] + 3 * v_B[0], 2 * v_A[1] + 3 * v_B[1], 2 * v_A[2] + 3 * v_B[2])
print("Combinazione lineare di mattoncini:", combinazione_lineare)
'''
In base a questo calcolo, il vettore 

(9,6,7) rappresenta:

2 mattoncini di tipo A (poiché  =2⋅(3,0,2)=(6,0,4))
3 mattoncini di tipo B (poiché  =3⋅(1,2,1)=(3,6,3))
Quindi, il vettore 
(9,6,7) rappresenta una combinazione di mattoncini di tipo A e B come descritto sopra.
'''
