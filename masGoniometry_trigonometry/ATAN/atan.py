import math
import matplotlib.pyplot as plt

# coordinate dei due punti
x1, y1 = 0.3, 0
x2, y2 = 1, 2

# calcolo dell'angolo tra i due punti
angolo = math.atan2(y2-y1, x2-x1)

# visualizzazione dei due punti e della linea che li collega
plt.plot([x1, x2], [y1, y2], '-o')
plt.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(facecolor='black', shrink=0.07))
plt.text((x1+x2)/2, (y1+y2)/2, '{:.2f}°'.format(math.degrees(angolo)))

# visualizzazione del grafico
plt.axis('equal')
plt.show()
