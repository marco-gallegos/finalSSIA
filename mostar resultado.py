# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# longitudes
xl = 10
yl = 10
zl = 10
num_lamparas = 2
# contenedor a partir de los limites
contenedor = [ [[0 for p1 in range(zl)] for p2 in range(yl)] for p3 in range(xl)]
contenedor = np.array(contenedor)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("Ancho")
ax.set_ylabel("Largo")
ax.set_zlabel("Alto")

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
                    if self.origen_y - y > 0:
                        newBox[self.origen_x][self.origen_y - y][i] = 1
                    if self.origen_x + x <= self.limite_x:
                        newBox[self.origen_x + x][self.origen_y][i] = 1
                    if self.origen_x + x > 0:
                        newBox[self.origen_x - x][self.origen_y][i] = 1
                    if self.origen_x + x <= self.limite_x and self.origen_y + y <= self.limite_y:
                        newBox[self.origen_x + x][self.origen_y + y ][i] = 1
                    if self.origen_x + x <= self.limite_x and self.origen_y - y > 0:
                        newBox[self.origen_x + x][self.origen_y - y ][i] = 1
                    if self.origen_x - x > 0 and self.origen_y + y <= self.limite_y:
                        newBox[self.origen_x - x][self.origen_y + y ][i] = 1
                    if self.origen_x - x > 0 and self.origen_y - y > 0:
                        newBox[self.origen_x - x][self.origen_y - y ][i] = 1

        return newBox

def renderBox(box, ax , xl, yl ,zl):
    """
    @param np.array[x][y][z] box -el contenedor a iluminar/ graficar
    @param plt.figure().add_subplot() ax -subplot para graficar
    """
    # imprimir esquinas limite
    ax.scatter3D([0],[0],[0])
    ax.scatter3D([0],[0],[zl])
    ax.scatter3D([0],[yl],[0])
    ax.scatter3D([0],[yl],[zl])
    ax.scatter3D([xl],[0],[0])
    ax.scatter3D([xl],[yl],[0])
    ax.scatter3D([xl],[yl],[zl])
    ax.scatter3D([xl],[0],[zl])
    for x in range(xl):
        for y in range(yl):
            for z in range(zl):
                if box[x][y][z] == 1:
                    ax.scatter3D([x],[y],[z])


def fitness(indiv,long_gen, num_lamparas):
    """
    el fitnes debe tomar un array binario donde los 1 representan la presencia de lamparas
    si tiene mas unos (lamparas) de lo necesario (num lamparas) por cada extra se suma 100 * (x + y)
    se debe convertir el array a una matriz x,y
    en cada 1 se debe renderizar un foco en la matriz
    el fitnes aumenta en 4 cada que encuentra un 0 en la matriz al ser una zona sin liminosidad
    """
    # print(x)
    fitnes = 0
    contenedor_muestra = [ [[0 for p1 in range(zl)] for p2 in range(yl)] for p3 in range(xl)]
    indiv_matriz = []
    tmp = []
    xi = 0
    for i in range(len(indiv)):
        tmp.append(indiv[i])
        if len(tmp) == long_gen:
            indiv_matriz.append(tmp)
            xi += 1
            tmp=[]
    
    if tmp != []:
        print("error de longitud")
        return 10000000
    
    # plot bulbos
    numero_bulbos = 0
    for x in range(xi):
        for y in range(long_gen):
            if indiv_matriz[x][y] == 1:
                numero_bulbos += 1
                if numero_bulbos > num_lamparas:
                    fitnes += 1000
                    
                bulbo_tmp = Bulbo(origen_x=x, origen_y=y, aumento_z=1, limite_x=xl-1,limite_y=yl-1,limite_z=zl)
                contenedor_muestra = bulbo_tmp.render(contenedor_muestra)
    for x in range(len(contenedor_muestra)):
        for y in range(len(contenedor_muestra[0])):
            for z in range(len(contenedor_muestra[0][0])):
                if contenedor_muestra[x][y][z] == 0:
                    fitnes += 1
    # menos focos de los requeridos
    fitnes += (num_lamparas - numero_bulbos) * 100
    # print(f"fitness : {fitnes}")
    return fitnes


def obtenerMatrizIndiv(indiv,long_gen):
    indiv_matriz = []
    tmp = []
    xi = 0
    for i in range(len(indiv)):
        tmp.append(indiv[i])
        if len(tmp) == long_gen:
            indiv_matriz.append(tmp)
            xi += 1
            tmp=[]
    if tmp != []:
        print("error de longitud")
    return indiv_matriz

sujeto = np.load("ultima_ejecucion.npy")
sujeto_fitnes = fitness(indiv=sujeto, long_gen=yl, num_lamparas=2)
print(f"Longitud : {len(sujeto)}\nfitnes {sujeto_fitnes}\nsujeto : \n{sujeto}")

sujeto2d = obtenerMatrizIndiv(sujeto, yl)

for x in range(len(sujeto2d)):
    for y in range(len(sujeto2d[x])):
        if sujeto2d[x][y] == 1:
            nuevo_bulbo = Bulbo(origen_x=x, origen_y=y, aumento_z=1, limite_x=xl-1, limite_y=yl-1, limite_z=zl)
            contenedor = nuevo_bulbo.render(contenedor)

renderBox(box=contenedor, ax=ax, xl=xl, yl=yl, zl=zl)

plt.show()
