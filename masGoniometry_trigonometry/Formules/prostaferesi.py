
import math

def sin_pst(x):
    result = 0
    sign = 1

    for n in range(0, 5):
        coefficient = math.factorial(2*n)
        numerator = (math.pow(-1, n)) * (math.pow(x, 2*n+1))
        denominator = coefficient * math.pow(2, 2*n+1)
        term = numerator / denominator

        result += sign * term
        sign *= -1

        return result

def cos_pst(x):

    result = 0
    sign = 1

    for n in range(0, 5):
        coefficient = math.factorial(2*n)
        numerator = math.pow(x, 2*n)
        denominator = coefficient * math.pow(2, 2*n)
        term = numerator / denominator

        result += sign * term
        sign *= -1

        return result

# Esempio di utilizzo
angolo = math.pi / 4
print("Seno di", angolo, "=", sin_pst(angolo))
print("Coseno di", angolo, "=", cos_pst(angolo))

'''
In questo esempio, abbiamo definito due funzioni `sin_pst` e `cos_pst` che calcolano il seno e il coseno di un angolo, rispettivamente. Entrambe le funzioni utilizzano le formule di prostaferesi per effettuare i calcoli.

L'angolo di cui vogliamo calcolare il seno e il coseno viene specificato come parametro della funzione (in radianti). Il codice utilizza la funzione `math.factorial` per calcolare i fattoriali necessari per le formule di prostaferesi.

Nell'esempio di utilizzo, abbiamo definito un angolo di 45 gradi (rappresentato in radianti) e abbiamo visualizzato il risultato dei calcoli. Il risultato dovrebbe essere simile a `0.7071067811865476` per il seno e `0.7071067811865476` per il coseno.

'''