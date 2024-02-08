'''
I margini di guadagno e fase forniscono informazioni cruciali sulla stabilità del sistema. Il margine di guadagno indica di quanto il guadagno del sistema può essere aumentato prima che il sistema diventi instabile, mentre il margine di fase indica di quanto la fase del sistema può essere aumentata prima che si verifichi l'instabilità.
I margini di guadagno e fase possono essere calcolati utilizzando il diagramma di Nyquist o il diagramma di Bode. Tuttavia, senza informazioni specifiche sul diagramma di Nyquist per la funzione di trasferimento data, non è possibile fornire i valori esatti dei margini di guadagno e fase per i due casi specifici.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definizione della funzione di trasferimento
def transfer_function(s, K):
    return signal.TransferFunction([K], [1, 6, 5, 0])

# Valori di K
K_values = [10, 100]

# Frequenze di valutazione per il diagramma di Nyquist
omega = np.logspace(-2, 3, 1000)

for K in K_values:
    # Calcolo della funzione di trasferimento per il valore di K corrente
    sys = transfer_function(1j * omega, K)

    # Diagramma di Nyquist
    _, nyquist, _ = signal.nyquist(sys)

    # Plot del diagramma di Nyquist
    plt.plot(nyquist.real, nyquist.imag, label=f'K = {K}')

    # Calcolo dei margini di guadagno e fase
    gm, pm, _, _ = signal.margin(sys)
    print(f"Margini di guadagno e fase per K = {K}:")
    print(f"Margine di guadagno: {gm}")
    print(f"Margine di fase: {pm}°")

# Plot delle linee degli assi reali e immaginari
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Etichette degli assi
plt.xlabel('Re')
plt.ylabel('Im')

# Titolo del grafico
plt.title('Diagramma di Nyquist')

# Aggiunta della legenda
plt.legend()

# Mostra il grafico
plt.show()
