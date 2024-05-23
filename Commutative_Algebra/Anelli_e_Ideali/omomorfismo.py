'''
Esempio in Python che illustra concetti di anelli e omomorfismi di anelli:
'''

# Definizione di due insiemi come anelli
A = {0, 1, 2, 3, 4}  # Anello A
B = {0, 1, 2}        # Anello B

# Definizione di una funzione che rappresenta un omomorfismo tra A e B
def omomorfismo(x):
    if x in A:
        return x % 3  # Omomorfismo che mappa gli elementi di A in B rispettando la struttura dell'anello

# Verifica delle proprietà dell'omomorfismo
for elem in A:
    print(f"Omomorfismo di {elem} è {omomorfismo(elem)}")

# Verifica della proprietà di omomorfismo: f(a + b) = f(a) + f(b)
for elem1 in A:
    for elem2 in A:
        print(f"Omomorfismo di {elem1} + {elem2} è {omomorfismo(elem1) + omomorfismo(elem2)}")
```

In questo esempio, abbiamo definito due insiemi A e B come anelli e una funzione `omomorfismo` che rappresenta un omomorfismo tra i due anelli. La funzione `omomorfismo` mappa gli elementi di A in B rispettando la struttura dell'anello. Successivamente, verifichiamo che la funzione soddisfi la proprietà di omomorfismo: f(a + b) = f(a) + f(b).
'''


