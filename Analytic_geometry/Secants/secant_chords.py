import turtle
import math

# Define the midpoint of the chords
x1, y1 = -100, 0
x2, y2 = 100, 0

# Define the points on the chords
xa, ya = -200, 150
xb, yb = -100, -80
xc, yc = 50, 100
xd, yd = 200, -100

# Calculate the slopes of the chords
ma = (ya - yb) / (xa - xb)
mb = (yb - yc) / (xb - xc)
mc = (yc - yd) / (xc - xd)
md = (yd - ya) / (xd - xa)

# Calculate the midpoints of the chords
mx1 = (xa + ya) / 2
my1 = (ya + yd) / 2
mx2 = (xb + xc) / 2
my2 = (yb + yc) / 2

# Calculate the slopes of the lines connecting the midpoints and the center of the circle
m1 = (my1 - y1) / (mx1 - x1)
m2 = (my2 - y1) / (mx2 - x1)

# Calculate the intersection point of the lines connecting the midpoints and the center of the circle
xint = (m2*x2 - y2 + y1 - m1*x1) / (m2 - m1)
yint = m1*(xint - x1) + y1

# Calculate the distance between the center of the circle and the intersection point
distance = math.sqrt((xint - x1)**2 + (yint - y1)**2)

# Set up the turtle window
turtle.speed(0)
turtle.bgcolor("white")
turtle.pensize(2)

# Draw the circle
turtle.penup()
turtle.goto(x1, y1 - distance)
turtle.pendown()
turtle.circle(distance)

# Draw the chords
turtle.penup()
turtle.goto(xa, ya)
turtle.pendown()
turtle.goto(xb, yb)

turtle.penup()
turtle.goto(xc, yc)
turtle.pendown()
turtle.goto(xd, yd)

# Draw the midpoints
turtle.penup()
turtle.goto(mx1, my1)
turtle.pendown()
turtle.dot(10)
turtle.write("M1")

turtle.penup()
turtle.goto(mx2, my2)
turtle.pendown()
turtle.dot(10)
turtle.write("M2")

# Draw the intersection point
turtle.penup()
turtle.goto(xint, yint)
turtle.pendown()
turtle.dot(10, "red")
turtle.write("Intersection")

# Draw the result
if distance > math.sqrt((xint - xa)**2 + (yint - ya)**2) or distance > math.sqrt((xint - xb)**2 + (yint - yb)**2) or distance > math.sqrt((xint - xc)**2 + (yint - yc)**2) or distance > math.sqrt((xint - xd)**2 + (yint - yd)**2):
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.write("Chords do not intersect in the interior of the circle")
else:
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.write("Chords intersect in the interior of the circle")

turtle.done()
