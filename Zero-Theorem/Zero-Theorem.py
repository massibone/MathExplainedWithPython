
import numpy as np
roots_all = np.roots(coeffs)  # Tutte le roots (complesse)
print(roots_all)

print ("Teorema degli zeri per l'equazione exp(x)=x+2 " )
import math
n=int(input("Inserisci un numero intero n: "))
def f(t):
    return math.exp(t)-t-2
p=pow(10,-n)
x=0
while f(x)*f(x+p)>0:
    x=x+p
    print ("function e**x =  x+2   " )
    print ("in x=",round(x,2)," f(x)=",round(f(x),4))
    print ("in x=",round(x+p,2)," f(x)=",round(f(x+p),4))
    print ("Solution is between ",round(x,2)," e ",round(x+p,2))
