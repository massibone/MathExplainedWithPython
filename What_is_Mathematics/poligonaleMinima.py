'''
determinare la poligonale di minima lunghezza tra due punti A e B, entrambi situati su una retta l, in modo che il percorso sia perpendicolare a l, è possibile utilizzare un approccio geometrico.
'''
import matplotlib.pyplot as plt

# Coordinate dei punti A e B
xa, xb = 1, 5
ya, yb = 0, 0

# Calcola il punto C (metà strada tra A e B)
xc = (xa + xb) / 2
yc = 0

# Calcola la lunghezza del percorso
lunghezza_totale = abs(xb - xa)

# Crea un grafico
plt.figure(figsize=(8, 6))

# Traccia il percorso
plt.plot([xa, xc, xb], [ya, yc, yb], marker='o', color='blue')
plt.text(xa, ya, 'A', fontsize=12, ha='right')
plt.text(xb, yb, 'B', fontsize=12, ha='right')
plt.text(xc, yc, 'C', fontsize=12, ha='right')

# Imposta i limiti dell'asse x in base ai punti A e B
plt.xlim(min(xa, xb) - 1, max(xa, xb) + 1)

# Aggiungi etichette e titolo
plt.xlabel('Asse x')
plt.ylabel('Asse y')
plt.title(f'Percorso di minima lunghezza tra A e B: Lunghezza = {lunghezza_totale:.2f}')
plt.grid(True)

# Mostra il grafico
plt.show()
