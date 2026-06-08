import math

def Vo_Sa_Cone(radius, height):
    # Calculate Length of a Slide (Slant)
    l = math.sqrt(radius * radius + height * height)

    # Calculate the Surface Area
    SA = math.pi * radius * (radius + l)

    # Calculate the Volume
    Volume = (1.0/3) * math.pi * radius * radius * height

    # Calculate the Lateral Surface Area
    LSA = math.pi * radius  * l

    print("\n Length of a Side (Slant)of a Cone = %.2f" %l)
    print(" The Surface Area of a Cone = %.2f " %SA)
    print(" The Volume of a Cone = %.2f" %Volume)
    print(" The Lateral Surface Area of a Cone = %.2f " %LSA)

Vo_Sa_Cone(12,20)