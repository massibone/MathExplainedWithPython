def equation(a,b,c,d):
#solves equations of the
#form ax + b = cx + d'''
    return (d - b)/(a - c)

#example x + 10 = –4x + 16
x=equation(1,10,-4,16)
print(round(x, 2))
