import numpy as np
import matplotlib.pyplot as plt

# Definizione della formula della posizione
def posizione(t, g):
    return 0.5 * g * t**2

# Derivata della posizione rispetto al tempo per ottenere la velocità
def velocita(t, g):
    return g * t

# Parametri
accelerazione_gravitazionale = 9.8  # m/s^2
tempo = np.linspace(0, 5, 100)  # Tempi da 0 a 5 secondi

# Calcolo delle posizioni e velocità
posizioni = posizione(tempo, accelerazione_gravitazionale)
velocita_corrente = velocita(tempo, accelerazione_gravitazionale)

# Plot delle posizioni e della velocità
plt.figure(figsize=(12, 6))

# Plot della posizione
plt.subplot(2, 1, 1)
plt.plot(tempo, posizioni, label='Posizione')
plt.title('Posizione del corpo che cade liberamente')
plt.xlabel('Tempo (s)')
plt.ylabel('Posizione (m)')
plt.legend()

# Plot della velocità
plt.subplot(2, 1, 2)
plt.plot(tempo, velocita_corrente, label='Velocità')
plt.title('Velocità del corpo che cade liberamente')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocità (m/s)')
plt.legend()

plt.tight_layout()
plt.show()
