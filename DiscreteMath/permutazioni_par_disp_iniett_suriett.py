'''
Si consideri l’applicazione ff : I6 → I6 tale che
ff(1) = 3; ff(2) = 6; ff(3) = 1; ff(4) = 4; ff(5) = 2; ff(6) = 5:
Una permutazione è definita come dispari se può essere scomposta in un numero dispari di trasposizioni. Una trasposizione è una permutazione che scambia esattamente due elementi e lascia invariati gli altri. Una permutazione è definita come pari se può essere scomposta in un numero pari di trasposizioni.

Nel caso della funzione ff che hai fornito, possiamo rappresentarla come una composizione di trasposizioni:

ff = (1 3)(2 6)(4 4)(5 2)(6 5)
'''
def permutazione_pari():
    return [1, 3, 6, 4, 5, 2]
# Esempio di utilizzo della permutazione pari
print(permutazione_pari())  # Output: [1, 3, 6, 4, 5, 2]
'''
In questo caso, la permutazione [1, 3, 6, 4, 5, 2] può essere rappresentata come una composizione di tre trasposizioni (1 3), (2 6) e (5 2). Poiché il numero di trasposizioni è pari, questa permutazione è pari.

Permutazione dispari:
'''
def permutazione_dispari():
    return [3, 6, 1, 4, 2, 5]

# Esempio di utilizzo della permutazione dispari
print(permutazione_dispari())  # Output: [3, 6, 1, 4, 2, 5]
'''
Permutazione iniettiva:
'''
def permutazione_iniettiva():
    return [1, 2, 3, 4, 5, 6]

# Esempio di utilizzo della permutazione iniettiva
print(permutazione_iniettiva())  # Output: [1, 2, 3, 4, 5, 6]

#suriettiva
def permutazione_suriettiva():
    return [3, 6, 1, 4, 2, 5]

# Esempio di utilizzo della permutazione suriettiva
print(permutazione_suriettiva())  # Output: [3, 6, 1, 4, 2, 5]
