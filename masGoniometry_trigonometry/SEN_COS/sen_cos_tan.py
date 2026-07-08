import matplotlib.pyplot as plt
import math

grados = []
seno = []
coseno = []
tangent = []

for i in range(0,540):
	grados.append(i)
	radianes = (i* math.pi)/180
	seno.append(math.sin(radianes))
	coseno.append(math.cos(radianes))
	tangent.append(math.tan(radianes))

plt.ylim(-2,2)
plt.plot(grados,seno,"r")
plt.plot(grados,coseno,"c")
plt.plot(grados,tangent)
plt.show()