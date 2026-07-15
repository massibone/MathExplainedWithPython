import math
import turtle

# Inserire l'angolo in gradi
angolo = float(input("Inserisci un angolo in gradi: "))

# Convertiamo l'angolo in radianti
angolo_radiani = math.radians(angolo)

# Calcoliamo la lunghezza del lato del triangolo in base all'angolo
lunghezza_lato = 100 / math.sin(angolo_radiani)

# Disegnamo il triangolo utilizzando la libreria turtle
t = turtle.Turtle()
t.forward(lunghezza_lato)
t.left(180 - angolo)
t.forward(100)
t.left(180 - (90 - angolo))
t.forward(lunghezza_lato)
t.left(180)

# Visualizziamo la figura
turtle.done()

