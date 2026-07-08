import math
import numpy as np

A=np.array([1,0,0])
B=np.array([0,1,0])
C=np.array([0,0,1])
D=np.array([1,1,1])

a=np.linalg.norm(B-C)
b=np.linalg.norm(A-C)
c=np.linalg.norm(A-B)
d=np.linalg.norm(D-A)
e=np.linalg.norm(D-B)
f=np.linalg.norm(D-C)

V=(1/3)* np.absolute(np.dot(np.cross(B-A,C-A),D-A))

r=(3*V)/np.sqrt((a+b+f-e)*(a+c+e-f)*(b+c+d-a)*(b+d+f-c))

print("IL raggio è", r)
