'''
con = xz + yw   dovrebbe risultare multilineare e simmetrica
'''

import numpy as np

def is_multilinear_symmetric(f):
    # Verifica la linearità rispetto alla prima variabile
    def check_first_variable(A, B):
        alpha = 2
        beta = 3
        result1 = f(alpha * A + beta * A, B)
        result2 = alpha * f(A, B) + beta * f(A, B)
        return np.array_equal(result1, result2)
