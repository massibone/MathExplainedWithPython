import numpy as np

# Definiamo due vettori in R^3
vettore1 = np.array([1, 2, 3])
vettore2 = np.array([-2, 0, 1])

# Proprietà 1: Addizione di vettori
somma_vettori = vettore1 + vettore2
print("Proprietà 1: Addizione di vettori")
print("Vettore1 + Vettore2 =", somma_vettori)

# Proprietà 2: Moltiplicazione per uno scalare
scalars = [2, -0.5]
print("\nProprietà 2: Moltiplicazione per uno scalare")
for alpha in scalars:
    prodotto_scalare = alpha * vettore1
    print(f"{alpha} * Vettore1 =", prodotto_scalare)

# Proprietà 3: Elemento neutro dell'addizione
elemento_neutro = np.zeros(3)
print("\nProprietà 3: Elemento neutro dell'addizione")
print("Elemento neutro:", elemento_neutro)
print("Vettore1 + Elemento neutro =", vettore1 + elemento_neutro)

# Proprietà 4: Inverso additivo
inverso_vettore1 = -vettore1
print("\nProprietà 4: Inverso additivo")
print("Inverso di Vettore1:", inverso_vettore1)
print("Vettore1 + Inverso di Vettore1 =", vettore1 + inverso_vettore1)

# Proprietà 5: Associatività dell'addizione
vettore3 = np.array([0, -1, 2])
print("\nProprietà 5: Associatività dell'addizione")
print("(Vettore1 + Vettore2) + Vettore3 =", (vettore1 + vettore2) + vettore3)
print("Vettore1 + (Vettore2 + Vettore3) =", vettore1 + (vettore2 + vettore3))

# Proprietà 6: Proprietà distributiva
alpha = 2
beta = -1.5
print("\nProprietà 6: Proprietà distributiva")
print(f"{alpha} * (Vettore1 + Vettore2) =", alpha * (vettore1 + vettore2))
print(f"{alpha} * Vettore1 + {alpha} * Vettore2 =", alpha * vettore1 + alpha * vettore2)
print(f"({alpha} + {beta}) * Vettore1 =", (alpha + beta) * vettore1)
print(f"{alpha} * Vettore1 + {beta} * Vettore1 =", alpha * vettore1 + beta * vettore1)
