'''
x^2 + 4*(z+10)^2 = e^(-0.05*z)

x^2=e^(-0.05*z)-4*(z+10)^2 If B=e^(-0.05*z)-4*(z+10)^2>0, 
it has two solutions x=sqrt(B) and x=-sqrt(B). 
Find the range of z for which B>0 using dichotomy, 
then use linespace and plot two curves (x,z and -x,z)


Calculate each side of equation for a given x and z gridded.
Then I contour points that satisfy the equation. 
One side minus other equals to zero.


'''




import numpy as np
import matplotlib.pyplot as plt

z = -np.linspace(9,15,100)
x = np.linspace(-26,26,1000)

x,z = np.meshgrid(x,z)

Z = -np.exp(-0.05*z) +4*(z+10)**2 
X = x**2


plt.contour(x,z,(X+Z),[0])
plt.xlim([-1.5,1.5])
plt.ylim([-11.5,-8.5])