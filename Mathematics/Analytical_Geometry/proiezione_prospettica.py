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

# Definisci i punti dell'angolo dell'immagine risultante (come se fosse vista dall'alto)
points_B = np.float32([[0,0], [420,0], [0,594], [420,594]])

# Calcola la matrice di trasformazione prospettica
matrix = cv2.getPerspectiveTransform(points_A, points_B)

# Applica la trasformazione prospettica all'immagine originale
result = cv2.warpPerspective(img, matrix, (420, 594))

# Visualizza l'immagine originale e l'immagine risultante
cv2.imshow('Original Image', img)
cv2.imshow('Perspective Transformation', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
