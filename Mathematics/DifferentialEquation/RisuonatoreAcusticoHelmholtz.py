'''
Il risuonatore acustico di Helrnholtz è costituito (vedi fig. 5.3) da un recipiente V, di volume v, contenente aria, munito di un collo cilindrico F. Approssimativamente si può considerare l'aria contenuta nel collo come un tappo di massa
'''
import numpy as np
import matplotlib.pyplot as plt

# Definizione delle costanti
v = 0.1  # Volume del recipiente (m^3)
S = 0.001  # Area trasversale del collo (m^2)
L = 0.1  # Lunghezza del collo (m)
m_tappo = 0.1  # Massa del tappo d'aria (kg)
k = 1000  # Costante elastica del tappo d'aria (N/m)

# Frequenze di risonanza
def frequenza_risonanza(n):
    return (n / (2 * np.pi)) * np.sqrt(k / (m_tappo + (v * S) / (S * L)))

# Calcolo delle frequenze di risonanza per i primi 5 modi
n_values = np.arange(1, 6)
frequencies = frequenza_risonanza(n_values)

# Plot delle frequenze di risonanza
plt.figure(figsize=(8, 6))
plt.plot(n_values, frequencies, 'bo-', label='Frequenze di risonanza')
plt.xlabel('n (numero di modo)')
plt.ylabel('Frequenza di risonanza (Hz)')
plt.title('Frequenze di risonanza del risuonatore acustico di Helmholtz')
plt.grid(True)
plt.legend()
plt.show()
