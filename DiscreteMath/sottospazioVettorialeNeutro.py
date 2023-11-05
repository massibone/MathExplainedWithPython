
import numpy as np

# Matrice neutra (elemento neutro rispetto alla somma)
elemento_neutro = np.zeros((3, 3))

# Verifica che la matrice neutra appartenga al sottospazio
# S, cioè che la prima riga sia uguale a zero
elemento_neutro_appartiene_a_S = np.all(elemento_neutro[0] == 0)

print("L'elemento neutro appartiene a S?", elemento_neutro_appartiene_a_S)
