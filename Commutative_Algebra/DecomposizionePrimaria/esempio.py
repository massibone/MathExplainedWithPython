'''
Abbiamo l'ideale 𝐼 generato da x^2 e xy in un anello di polinomi 
k[x,y]:
I=(x^2 ,xy)

Possiamo decomporre 
𝐼  come un'intersezione di due ideali primari
'''
from sympy import symbols, Ideal, groebner

# Definiamo le variabili e l'anello dei polinomi
x, y = symbols('x y')
R = groebner([x**2, x*y])

# Definiamo l'ideale originale
I = Ideal(x**2, x*y)

# Decomposizione primaria dell'ideale
primary_decomposition = I.primary_decomposition()

# Visualizziamo la decomposizione
print("Decomposizione primaria dell'ideale (x^2, xy):")
for ideal in primary_decomposition:
    print(ideal)
