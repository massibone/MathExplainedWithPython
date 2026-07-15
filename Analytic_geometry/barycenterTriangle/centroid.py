if __name__ == "__main__" :
 
    # coordinate of the vertices
    x1, x2, x3 = 1, 3, 6
    y1, y2, y3 = 2, -4, -7
     
    # Formula to calculate centroid
    x = round((x1 + x2 + x3) / 3, 2)
    y = round((y1 + y2 + y3) / 3, 2)
 
    print("Centroid =","(",x,",",y,")")
 