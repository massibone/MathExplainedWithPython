import math

# coordinates of the triangle vertices
A = [-2, 0] # left point
B = [2, 0] # right point
C = [0, 3] # top point

# calculate the distances between the vertices
AB = math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
BC = math.sqrt((C[0]-B[0])**2 + (C[1]-B[1])**2)
AC = math.sqrt((C[0]-A[0])**2 + (C[1]-A[1])**2)

# check if AB is a diameter of the circle passing through A, B, and C
if AB == 2 * BC == 2 * AC:
    print("Thale's theorem is true.")
else:
    print("Thale's theorem is false.")

