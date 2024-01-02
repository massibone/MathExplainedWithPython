'''
data l' applicazione f. R^3 -> R^3
(x          -->         (2x+3z+1
y                             2y+z-1
z)                           x+y+2z+2)
'''
import numpy as np

def linear_application(vector):
    x, y, z = vector
    result_vector = np.array([2*x + 3*z, 2*y + z, x + y + 2*z])
    return result_vector

# Verifica additività
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

additivity_lhs = linear_application(u + v)
additivity_rhs = linear_application(u) + linear_application(v)

print("Additività:", np.array_equal(additivity_lhs, additivity_rhs))

# Verifica omogeneità scalare
alpha = 2
homogeneity_lhs = linear_application(alpha * u)
homogeneity_rhs = alpha * linear_application(u)

print("Omogeneità scalare:", np.array_equal(homogeneity_lhs, homogeneity_rhs))
