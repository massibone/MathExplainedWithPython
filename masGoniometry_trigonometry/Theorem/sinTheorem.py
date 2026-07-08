import turtle
import math

# Chiedi all'utente di inserire l'angolo in gradi
angolo_deg = float(input("Inserisci l'angolo in gradi: "))

# Converti l'angolo in radianti
angolo_rad = math.radians(angolo_deg)

# Calcola il seno dell'angolo
seno_angolo = math.sin(angolo_rad)

# Calcola i lati del triangolo proporzionali al seno dell'angolo
lato_a = 100 * seno_angolo
lato_b = 150 * seno_angolo
lato_c = 200 * seno_angolo

# Disegna il triangolo usando il modulo Turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-lato_b/2, 0)
turtle.pendown()
turtle.forward(lato_b)
turtle.left(180 - angolo_deg)
turtle.forward(lato_a)
turtle.left(180 - (90 - angolo_deg))
turtle.forward(lato_c)
turtle.hideturtle()

turtle.done()