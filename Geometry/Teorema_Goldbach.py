'''
 Il Teorema di Goldbach afferma che ogni numero pari 
 maggiore di 2 può essere espresso come somma di due 
 numeri primi.

Ad esempio, il numero 8 può essere espresso 
come la somma dei numeri primi 3 e 5, 
poiché 3 + 5 = 8. Allo stesso modo, 
il numero 20 può essere espresso come 
la somma dei numeri primi 7 e 13, 
poiché 7 + 13 = 20.
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_conjecture(limit):
    primes = [i for i in range(2, limit) if is_prime(i)]
    even_composites = [num for num in range(4, limit, 2) if not is_prime(num)]
    
    goldbach_numbers = []
    for composite in even_composites:
        found = False
        for prime in primes:
            if prime > composite:
                break
            if is_prime(composite - prime):
                found = True
                break
        if not found:
            goldbach_numbers.append(composite)
    
    return goldbach_numbers[:100]

# Trova i primi 100 numeri pari esprimibili come somma di due numeri primi
result = goldbach_conjecture(1000)
print(result)
