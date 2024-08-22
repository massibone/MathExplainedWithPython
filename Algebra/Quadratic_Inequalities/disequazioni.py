
import math

a = float(input("insert a: "))
b = float(input("insert b: "))
c = float(input("insert c: "))
sign = str(input("Insert sign > or <:  "))
if c == 0:
    d = b**2-4*a*1
else:
    d = b**2-4*a*c


print("Disequation is: ", a, "x^2 +", b, "x +", c, sign, "0")


if d < 0 and a > 0:
    print("No intersection , no real solution")

if d < 0 and a < 0:
    print("Solution in R is void")


if d >= 0 and a > 0 and sign == ">":
    x1 = ((-b) + math.sqrt(d))/(2*a)
    x2 = ((-b) - math.sqrt(d))/(2*a)
    if x1 < x2:
        print("Solutions roots external\n")
        print("x <", x1, "e x >", x2)
    else:
        print("Solutions roots external\n")
        print("x <", x2, "e x >", x1)
if d >= 0 and sign == "<":
    print("Solutions roots internal\n")
    x1 = ((-b) + math.sqrt(d))/(2*a)
    x2 = ((-b) - math.sqrt(d))/(2*a)
    if x1 > x2:
        print(" ", x2, "< x <", x1)
    else:
        print(" ", x1, "< x <", x2)
