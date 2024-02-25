def momento_inerzia_sistema(masse, coordinate_punti, punto_p):
    M = 0
    
    for i in range(len(masse)):
        # Calcola la distanza tra il punto P e il punto i
        r = ((coordinate_punti[i][0] - punto_p[0])**2 +
             (coordinate_punti[i][1] - punto_p[1])**2 +
             (coordinate_punti[i][2] - punto_p[2])**2) ** 0.5
