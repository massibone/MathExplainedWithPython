import math
 
# Function to find distance
def shortest_distance(x1, y1, a, b, c):
      
    d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
    print("Perpendicular distance is",d)

# Driver Code
x1 = 5
y1 = 6
a = -2
b = 3
c = 4
shortest_distance(x1, y1, a, b, c) 
