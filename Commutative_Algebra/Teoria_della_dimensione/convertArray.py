
'''
conversione di un'immagine in un array di numeri 
con caratteristiche di Hilbert richiede diverse librerie e passaggi dettagliati. Per fornirti un esempio utile e contestuale, avrei bisogno di informazioni specifiche sulle caratteristiche di Hilbert che ti interessano (ad esempio, intensità, texture, Carr) e sul formato delle immagini (ad esempio, JPG, PNG).
'''
import numpy as np
from skimage import io
from scipy.fftpack import hfft, iffhfft

# Caricamento dell'immagine
immagine = io.imread('immagine.jpg')

# Conversione in scala di grigi
immagine = immagine.astype('float32') / 255.0
