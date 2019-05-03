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

xl = yl = zl = 20
# contenedor a partir de los limites
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

class Bulbo:
    def __init__(self, origen_x, origen_y, aumento_z, limite_x, limite_y, limite_z):
        self.origen_x = origen_x
        self.origen_y = origen_y
        self.aumento_z = aumento_z
        self.limite_x = limite_x
        self.limite_y = limite_y
        self.limite_z = limite_z
    
    def render(self,box):
        """
        Representar el bulbo e el box
        @param np.array[x][y][z] solos los dos 
        """
        newBox = box
        for i in range(self.limite_z):
            for x in range(i):
                for y in range(i):
                    if self.origen_y + y <= self.limite_y:
                        newBox[self.origen_x][self.origen_y + y][i] = 1
                    if self.origen_y - y >= 0:
                        newBox[self.origen_x][self.origen_y - y][i] = 1
                    if self.origen_x + x <= self.limite_x:
                        newBox[self.origen_x + x][self.origen_y][i] = 1
                    if self.origen_x + x >= 0:
                        newBox[self.origen_x - x][self.origen_y][i] = 1
                    if self.origen_x + x <= self.limite_x and self.origen_y + y <= self.limite_y:
                        newBox[self.origen_x + x][self.origen_y + y ][i] = 1
                    if self.origen_x + x <= self.limite_x and self.origen_y - y >= 0:
                        newBox[self.origen_x + x][self.origen_y - y ][i] = 1
                    if self.origen_x - x >= 0 and self.origen_y + y <= self.limite_y:
                        newBox[self.origen_x - x][self.origen_y + y ][i] = 1
                    if self.origen_x - x >= 0 and self.origen_y - y >= 0:
                        newBox[self.origen_x - x][self.origen_y - y ][i] = 1

        return newBox
        
# declaracion de un bulbo
mi_bulbo = Bulbo(origen_x=18,origen_y=18,aumento_z=1,limite_x=19,limite_y=19,limite_z=10)
#fin de declaracion de un bulbo

    
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("Ancho")
ax.set_ylabel("Largo")
ax.set_zlabel("Alto")

#plot sobre nuestro contenedor
contenedor = mi_bulbo.render(contenedor)

printBox(contenedor, ax, xl, yl, zl)
# ax.scatter3D(x,y,z)
plt.show()