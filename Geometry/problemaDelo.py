'''
" problema di Delo "; poiché i sacerdoti di Apollo nell'isola di Delo avevano posto a un frequentatore 
dell'oracolo il problema di raddoppiare il volume del loro altare 
di marmo. Ora quest'altare era cubico e un cubo di volume doppio 
avrebbe dovuto avere uno spigolo radice terza di 2. volte quello dato. 
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Dimensione del cubo originale
lato_cubo_originale = 1

# Calcola la dimensione del cubo raddoppiato
lato_cubo_raddoppiato = lato_cubo_originale * (2 ** (1/3))

# Vertici del cubo originale
vertici_cubo_originale = [
    [0, 0, 0],
    [lato_cubo_originale, 0, 0],
    [lato_cubo_originale, lato_cubo_originale, 0],
    [0, lato_cubo_originale, 0],
    [0, 0, lato_cubo_originale],
    [lato_cubo_originale, 0, lato_cubo_originale],
    [lato_cubo_originale, lato_cubo_originale, lato_cubo_originale],
    [0, lato_cubo_originale, lato_cubo_originale]
]

# Vertici del cubo raddoppiato
vertici_cubo_raddoppiato = [
    [0, 0, 0],
    [lato_cubo_raddoppiato, 0, 0],
    [lato_cubo_raddoppiato, lato_cubo_raddoppiato, 0],
    [0, lato_cubo_raddoppiato, 0],
    [0, 0, lato_cubo_raddoppiato],
    [lato_cubo_raddoppiato, 0, lato_cubo_raddoppiato],
    [lato_cubo_raddoppiato, lato_cubo_raddoppiato, lato_cubo_raddoppiato],
    [0, lato_cubo_raddoppiato, lato_cubo_raddoppiato]
]

# Facciate del cubo originale
facciate_cubo_originale = [
    [vertici_cubo_originale[0], vertici_cubo_originale[1], vertici_cubo_originale[2], vertici_cubo_originale[3]],
    [vertici_cubo_originale[4], vertici_cubo_originale[5], vertici_cubo_originale[6], vertici_cubo_originale[7]],
    [vertici_cubo_originale[0], vertici_cubo_originale[1], vertici_cubo_originale[5], vertici_cubo_originale[4]],
    [vertici_cubo_originale[2], vertici_cubo_originale[3], vertici_cubo_originale[7], vertici_cubo_originale[6]],
    [vertici_cubo_originale[0], vertici_cubo_originale[3], vertici_cubo_originale[7], vertici_cubo_originale[4]],
    [vertici_cubo_originale[1], vertici_cubo_originale[2], vertici_cubo_originale[6], vertici_cubo_originale[5]]
]

# Facciate del cubo raddoppiato
facciate_cubo_raddoppiato = [
    [vertici_cubo_raddoppiato[0], vertici_cubo_raddoppiato[1], vertici_cubo_raddoppiato[2], vertici_cubo_raddoppiato[3]],
    [vertici_cubo_raddoppiato[4], vertici_cubo_raddoppiato[5], vertici_cubo_raddoppiato[6], vertici_cubo_raddoppiato[7]],
    [vertici_cubo_raddoppiato[0], vertici_cubo_raddoppiato[1], vertici_cubo_raddoppiato[5], vertici_cubo_raddoppiato[4]],
    [vertici_cubo_raddoppiato[2], vertici_cubo_raddoppiato[3], vertici_cubo_raddoppiato[7], vertici_cubo_raddoppiato[6]],
    [vertici_cubo_raddoppiato[0], vertici_cubo_raddoppiato[3], vertici_cubo_raddoppiato[7], vertici_cubo_raddoppiato[4]],
    [vertici_cubo_raddoppiato[1], vertici_cubo_raddoppiato[2], vertici_cubo_raddoppiato[6], vertici_cubo_raddoppiato[5]]
]

# Crea una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Aggiungi le facciate del cubo originale
ax.add_collection3d(Poly3DCollection(facciate_cubo_originale, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Aggiungi le facciate del cubo raddoppiato
ax.add_collection3d(Poly3DCollection(facciate_cubo_raddoppiato, facecolors='magenta', linewidths=1, edgecolors='b', alpha=.25))

# Imposta i limiti dell'asse
ax.set_xlim([0, lato_cubo_raddoppiato])
ax.set_ylim([0, lato_cubo_raddoppiato])
ax.set_zlim([0, lato_cubo_raddoppiato])

# Etichette degli assi
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
