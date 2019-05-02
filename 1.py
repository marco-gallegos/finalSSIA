# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:32:37 2019

el objetivo es tener un array de 3 dimensiones que indique en 1 o 0
si el epacio esta iluminado o no
eventualmente crear funcion para graficar el espacio

* limite en x, y ,z son la dimension de mi array
* plot this array
* crear luminaria
    * esta tiene un origen
    * limites en z (altura)
* funcion plot en luminaria que tome el array y ponga 1 donde esta ilumina

@author: Marco Gallegos
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

xl = yl = zl = 30
contenedor = [ [[0 for p1 in range(zl)] for p2 in range(yl)] for p3 in range(xl)]
contenedor = np.array(contenedor)


def printBox(box, ax , xl, yl ,zl):
    """
    @param np.array[x][y][z] box -el contenedor a iluminar/ graficar
    @param plt.figure().add_subplot() ax -subplot para graficar
    """
    for x in range(xl):
        for y in range(yl):
            for z in range(zl):
                if box[x][y][z] == 1:
                    ax.scatter3D([x],[y],[z])

def Luminaria(Object):
    def __init__(self, origen, aumento_z, limite_z):
        self.origen = origen
        self.aumento_z = aumento_z
        self.limite_z = limite_z
        

    
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("Ancho")
ax.set_ylabel("Largo")
ax.set_zlabel("Alto")

printBox(contenedor, ax, xl, yl, zl)
# ax.scatter3D(x,y,z)
plt.show()