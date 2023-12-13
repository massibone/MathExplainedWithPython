'''
Per determinare se l'applicazione sia multilineare, dobbiamo verificare la linearità rispetto 
a ciascuna delle sue variabili. Un'applicazione è multilineare 
se è lineare in ciascuna variabile quando l'altra è fissata.
'''


def is_multilinear(f):
    # Verifica la linearità rispetto alla prima variabile
    def check_first_variable(A, B):
        alpha = 2
        beta = 3
        result1 = f(alpha * A + beta * A, B)
        result2 = alpha * f(A, B) + beta * f(A, B)
        return result1 == result2

    # Verifica la linearità rispetto alla seconda variabile
    def check_second_variable(A, B):
        alpha = 2
        beta = 3
        result1 = f(A, alpha * B + beta * B)
        result2 = alpha * f(A, B) + beta * f(A, B)
        return result1 == result2

    # Esegui i test per verificare la linearità rispetto alle variabili
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    if check_first_variable(A, B) and check_second_variable(A, B):
        return True
    else:
        return False

# Esempio di applicazione
def f(A, B):
    result = [[3 * A[0][0] - A[0][1], A[1][0] + A[1][1] + 1], [0, 1]]
    return result

# Verifica se l'applicazione è multilineare
if is_multilinear(f):
    print("L'applicazione è multilineare.")
else:
    print("L'applicazione non è multilineare.")
