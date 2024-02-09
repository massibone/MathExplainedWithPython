import numpy as np
import math
import matplotlib.pyplot as plt 

phi1=np.pi/4.#math.radians() 
V1M=10 
V1=V1M*math.sin(2*np.pi+phi1) 
MV1=abs(V1M) 
ReV1=MV1*math.cos(phi1) 
ImV1=MV1*math.sin(phi1) 
print (ReV1,ImV1 )
c1=complex(ReV1,ImV1) 
phi2=np.pi/6. 
V2M=10 
V2=V2M*math.sin(2*np.pi+phi2) 
MV2=abs(V2M) 
ReV2=MV2*math.cos(phi2) 
ImV2=MV2*math.sin(phi2) 
print (ReV2,ImV2 )
c2=complex(ReV2,ImV2) 
c3=c1+c2 
import cmath 
print (c3.real,c3.imag,abs(c3),cmath.phase(c3) )
plt.arrow(0,0,c1.real,c1.imag, head_width=0.2, head_length=0.2, fc='lightblue', ec='black', length_includes_head=True) 
plt.arrow(0,0,c2.real,c2.imag, head_width=0.2, head_length=0.2, fc='lightblue', ec='black', length_includes_head=True) 
plt.arrow(0,0,c3.real,c3.imag, head_width=0.2, head_length=0.2, fc='lightblue', ec='red', length_includes_head=True) 
plt.grid()
plt.xlim(0,20) 
plt.ylim(0,20) 
plt.show() 
plt.close() 