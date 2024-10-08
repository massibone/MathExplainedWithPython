'''
How to solve Quadratic Equation

Risolve equazioni di secondo grado e i risultati 0,75 lo visualizza come frazione ( 3/4) 
Inserire valori di a,b,c con la virgola es 4x^2-3x=0 inseriro' 4,-3,0
'''


from math import sqrt
from fractions import Fraction


def dec_to_proper_frac(dec):
    sign = "-" if dec < 0 else ""
    frac = Fraction(abs(dec))
    return (f"{sign}{frac.numerator // frac.denominator} "
            f"{frac.numerator % frac.denominator}/{frac.denominator}")


# ax2 ± bx ± c = 0
check_input = True
while check_input:
    a, b, c = eval(
        input("Please enter the a, b, c example insert with comma 4,7,3 : "))
    try:
        float(a), float(b), float(c)
        check_input = False
    except ValueError:
        print("Please make sure the coefficients are real numbers and try again")
        check_input = True

print(f'{a}x^2', end='')
#print(a, 'x^2', sep='')
print(f'{b:+}''x', end='')
print(f'{c:+}', '= 0')


disc = b*b-4*a*c

if disc >= 0:
    x1 = (-b+sqrt(disc))/(2*a)
    x2 = (-b-sqrt(disc))/(2*a)
    dec_to_proper_frac(x1)
    dec_to_proper_frac(x2)
    print("The two solution of the equation are:",
          Fraction(str(x1)),  Fraction(str(x2))
else:
    print("The equation has no solutions")  
