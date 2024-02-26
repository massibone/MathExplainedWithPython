def momento_inerzia_sistema(masse, coordinate_punti, punto_p):
    M = 0
        for i in range(len(masse)):
        # Calcola la distanza tra il punto P e il punto i
        r = ((coordinate_punti[i][0] - punto_p[0])**2 +
             (coordinate_punti[i][1] - punto_p[1])**2 +
             (coordinate_punti[i][2] - punto_p[2])**2) ** 0.5
     # Calcola il momento di inerzia del punto i rispetto al punto P
        I = masse[i] * r**2
        
        # Aggiungi il momento di inerzia parziale al momento totale
        M += I

    return M

# Esempio di utilizzo
masse = [m1, m2, m3]  # sostituire con le masse effettive
coordinate_punti = [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]  # sostituire con le coordinate effettive
punto_P = (x, y, z)  # sostituire con le coordinate effettive

momento_inerzia_totale = momento_inerzia_sistema(masse, coordinate_punti, punto_P)
print("Momento di inerzia totale:", momento_inerzia_totale)
