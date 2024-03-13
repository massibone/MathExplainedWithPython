'''
Come stabilire se una eq algebrica a coeff reali ha almeno una radice reale
'''
def sturm_sequence(polynomial):
    sturm_seq = [polynomial, polynomial.deriv()]
    while sturm_seq[-1] != 0:
        remainder = sturm_seq[-2] % sturm_seq[-1]
        sturm_seq.append(-remainder)
    return sturm_seq[:-1]

def sign_changes_at_infinity(sturm_seq):
    return sum(1 for coeff in sturm_seq[0] if coeff < 0) % 2

def count_real_roots(polynomial, a, b):
    sturm_seq = sturm_sequence(polynomial)
    changes_at_a = sign_changes_at_infinity([poly.subs(x, a) for poly in sturm_seq])
    changes_at_b = sign_changes_at_infinity([poly.subs(x, b) for poly in sturm_seq])
    return changes_at_a - changes_at_b

from sympy import symbols

x = symbols('x')
polynomial = x**3 - 2*x**2 - 3*x + 4
a = -10  # Limite inferiore dell'intervallo
b = 10   # Limite superiore dell'intervallo

num_real_roots = count_real_roots(polynomial, a, b)
print("Numero di radici reali distinte nell'intervallo [{}, {}]: {}".format(a, b, num_real_roots))
