import matplotlib.pyplot as plt 
import numpy as np 
P1=[2,4] 
X=np.arange(-5,5,0.5) 
Y=np.polyval(P1,X) 
plt.plot(X,Y,"ko-") 
P2=[1,0,0] 
Y=np.polyval(P2,X) 
plt.plot(X,Y,"r*-") 
plt.grid(True) 
plt.show() 
