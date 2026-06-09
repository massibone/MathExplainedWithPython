import math
base = input ("Misura della base: ")
altezza = input ("Misura dell'altezza: ")
lato1 = input ("Misura del lato 2: ")
lato2 = input ("Misura del lato 3: ")
      
'''
A prism is said to be right when its lateral edges are perpendicular to the planes 
of the bases. It is evident that in a right prism 
the lateral faces are rectangles and that the lateral edges are
equal to the height.
'''




def prisma_retto(base, altezza, lato1, lato2):
   area = (int(base) * int(altezza)) / 2
   perimetro = int(base) + int(lato1) + int(lato2)
   superficie_laterale = perimetro * int(altezza)
   superficie_totale = superficie_laterale + ( 2 * area)
   volume = int(area) * int(altezza)
   
   return superficie_laterale, superficie_totale, volume
   
print("La superficie laterale, totale, e il volume sono rispettivamente:", prisma_retto(base, altezza, lato1, lato2))
