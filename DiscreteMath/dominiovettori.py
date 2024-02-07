import matplotlib.pyplot as plt 
P1=[2,4] 
D=[3,2] #N.B. !!! Lunghezza del vettore lungo x e y 
plt.arrow(P1[0],P1[1],D[0],D[1], head_width=0.2, head_length=0.2, fc='lightblue', ec='black', 
length_includes_head=True) 
plt.grid() 
plt.xlim(0,10) 
plt.ylim(0,10) 
plt.show() 
plt.close()