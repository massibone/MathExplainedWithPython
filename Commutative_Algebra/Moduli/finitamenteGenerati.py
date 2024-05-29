import numpy as np

# Definiamo una lista di vettori che generano il modulo
v1 = np.array([1, 0, 0])  # Vettore (1, 0, 0)
v2 = np.array([0, 1, 0])  # Vettore (0, 1, 0)
v3 = np.array([0, 0, 1])  # Vettore (0, 0, 1)

# Creiamo un modulo finitamente generato usando questi vettori
modulo_generato = [v1, v2, v3]

# Ora possiamo combinare questi vettori per creare altri vettori nel modulo
# Ad esempio, possiamo creare il vettore (1, 1, 1) come combinazione lineare di v1, v2 e v3
combinazione_lineare = 2 * v1 + (-1) * v2 + 3 * v3

# Stampiamo il modulo generato e la combinazione lineare risultante
print("Modulo finitamente generato:", modulo_generato)
print("Combinazione lineare:", combinazione_lineare)
