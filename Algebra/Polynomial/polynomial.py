import numpy

p=(numpy.poly1d([1,2,7,4,8]))
print("Polynomial is:  ",p,"= 0")

print("The solution(s) : ")
print(p.roots)
