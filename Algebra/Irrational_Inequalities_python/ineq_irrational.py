
#sqrt(Ax) < Bx is equivalent to system 
# A(x) >= 0, B(x) > 0, A(x)< (B(x))**2
#example sqrt(5-x) < x+1  solution are 1<x<=5
# is sign is <= symply add  B(x) >= 0, A(x)<= (B(x))**2

from sympy import *
init_printing()

x = Symbol('x')
a=5
b=1
if a>=0 and b>0:
    eq1=(5-x)>=0
    eq2=(x+1)>0
    eq2a=(5-x)<(x+1)**2

    

    sistem1=(solve([eq1,eq2,eq2a]))
    
    print("Irrational inequalities sign < or <=")
    print(sistem1)
 # irrational inequalities sign > or >=
 #example sqrt(-2x+7) > x-2 system are
 # x-2<0             x-2>=0
 # -2x+7>=0         -2x+7>(x-2)**2
 # the final solution is  x < 3
 # For sign >= symply add
 # x-2<0             x-2>=0
 # -2x+7>=0         -2x+7 >=   (x-2)**2
eq3=(x-2)<0
eq4=(-2*x+7)>=0

eq5=(x-2)>=0
eq6=(-2*x+7)>(x-2)**2

sistem2=(solve([eq3,eq4]))
sistem3=(solve([eq5,eq6]))

print(sistem2,sistem3)
