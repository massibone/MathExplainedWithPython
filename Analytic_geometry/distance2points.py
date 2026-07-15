import math
  
# Two dimensional Point
  
# point a
x1 = 100
y1 = 200
# point b
x2 = 400
y2 = 300
# distance b/w a and b
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
# display the result
print("Distance between points ({}, {}) and ({}, {}) is {}".format(x1,y1,x2,y2,distance))