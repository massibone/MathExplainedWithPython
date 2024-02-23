'''
Questo esemio carica un'immagine, definisce i punti degli angoli dell'immagine originale e dell'immagine risultante (come se fosse vista dall'alto), 
calcola la matrice di trasformazione prospettica e applica questa trasformazione all'immagine originale.
Infine, visualizza sia l'immagine originale che l'immagine risultante utilizzando OpenCV.
'''
import cv2
import numpy as np

# Carica l'immagine
img = cv2.imread('image.jpg')

# Definisci i punti dell'angolo della tua immagine originale
points_A = np.float32([[320,15], [700,215], [85,610], [530,780]])
