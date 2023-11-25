mport numpy as np

def f(x, y, z):
    return np.array([x + 2*y + z, y + z])

def is_homomorphism(v1, v2):
    # Verifica la preservazione della somma
    sum_left = f(v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])
    sum_right = f(v1[0], v1[1], v1[2]) + f(v2[0], v2[1], v2[2])
    sum_preserved = np.array_equal(sum_left, sum_right)

    # Verifica la preservazione della moltiplicazione per scalare
    scalar = 2
    scalar_left = f(scalar * v1[0], scalar * v1[1], scalar * v1[2])
    scalar_right = scalar * f(v1[0], v1[1], v1[2])
    scalar_preserved = np.array_equal(scalar_left, scalar_right)

    return sum_preserved, scalar_preserved

# Esempio di vettori v1 e v2
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Verifica se f è un omomorfismo
print(is_homomorphism(v1, v2))
