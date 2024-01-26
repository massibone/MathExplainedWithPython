'''
data l' applicazione f. R^3 -> R^3
(x          -->         (2x+3z+1
y                             2y+z-1
z)                           x+y+2z+2)
come faccio a dire che è un'applicazione lineare?
'''

import numpy as np

def linear_application(vector):
    x, y, z = vector
    result_vector = np.array([2*x + 3*z + 1, 2*y + z - 1, x + y + 2*z + 2])
    return result_vector

# Esempio di utilizzo
input_vector = np.array([1, 2, 3])
output_vector = linear_application(input_vector)

print("Input Vector:", input_vector)
print("Output Vector:", output_vector)

