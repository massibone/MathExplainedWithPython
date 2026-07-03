import math
import matplotlib.pyplot as plt

# creiamo una lista di angoli in radianti da 0 a 2π
angoli = [i * 0.5 for i in range(70)]
arcotangenti = [math.atan(a) for a in angoli]

# disegniamo il grafico
plt.plot(angoli, arcotangenti)
plt.xlabel('Angolo (radianti)')
plt.ylabel('Arco tangente (radianti)')
plt.title('Arco tangente di un angolo in radianti')
plt.grid(True)
plt.show()
