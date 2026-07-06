'''
Nella circonferenza goniometrica la cotangente di un angolo alfa è l'inverso della tangente ed è pari al rapporto tra il coseno e il seno dell'angolo alfa. cot α=1tanα=cosαsinα ⁡ α = 1 tan 

The tangent function has period π. f(x)=Atan(Bx−C)+D is a tangent with vertical and/or horizontal stretch/compression and shift. The cotangent function has period π and vertical asymptotes at 0,±π,±2π,.... The range of cotangent is (−∞,∞), and the function is decreasing at each point in its range

'''



import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(0, 2*np.pi,100)

sin_theta=np.sin(theta)
cos_theta=np.cos(theta)
cot_theta=1/np.tan(theta)

plt.plot(np.cos(theta,np.sin(theta)))

plt.plot(cos_theta,sin_theta,label='sin/cos')
plt.plot(theta,cot_theta,label='cot')

plt.legend()
plt.show()