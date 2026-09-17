#import cmath for complex number operations
import cmath


#Polar vs Cartesian Coordinates - www.101computing.net/polar-vs-cartesian-coordinates/
import draw, math

#Generate (x,y)) plot them on the canvas
x,y = draw.cartesianCoordinates()

#Output Cartesian Coordinates
print("Cartesian Coordinates: (" + str(x) + "," + str(y) + ")")

#Calculate Polar Cooordinates
r = (x**2 + y**2)**0.5
theta = math.atan2(y,x)
#Convert from radians to degrees
theta = math.degrees(theta)

#Output polar Coordinates
print("Polar Coordinates: (" + str(round(r,2)) + "," + str(round(theta,2)) + "°)")

#find the polar coordinates of complex number
print (cmath.polar(2 + 3j))
print (cmath.polar(1 + 5j))
