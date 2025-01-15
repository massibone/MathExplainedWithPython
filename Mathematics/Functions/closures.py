def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

f = outer()
print(f())
print(f())
'''
Quando si chiama la funzione f() per la prima volta, essa incrementa la variabile x di 1 e la restituisce, che è 11.
Quando si chiama la funzione f() per la seconda volta, essa incrementa la variabile x di 1 (che ora ha valore 11) e la restituisce, che è 12.
'''
