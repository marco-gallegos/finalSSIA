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


# longitudes
xl = 10
yl = 10
zl = 10
# limites
limite_inferior = 0
limite_superior = 2
num_lamparas = 2
# contenedor a partir de los limites
contenedor = [ [[0 for p1 in range(zl)] for p2 in range(yl)] for p3 in range(xl)]
contenedor = np.array(contenedor)


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
        
# declaracion de un bulbo
# mi_bulbo = Bulbo(origen_x=15,origen_y=15,aumento_z=1,limite_x=xl-1,limite_y=yl-1,limite_z=zl)

    
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("Ancho")
ax.set_ylabel("Largo")
ax.set_zlabel("Alto")

#plot sobre nuestro contenedor
# contenedor = mi_bulbo.render(contenedor)

# rednderBox(contenedor, ax, xl, yl, zl)
# limpiar plt
# plt.clf()
# ax = fig.add_subplot(111, projection="3d")
# fin limpieza
# renderBox(contenedor, ax, xl, yl, zl)
# print("mostrando estado inicial")
# plt.show()


def fitness(indiv,long_gen, num_lamparas, contenedor_vacio):
    """
    el fitnes debe tomar un array binario donde los 1 representan la presencia de lamparas
    si tiene mas unos (lamparas) de lo necesario (num lamparas) por cada extra se suma 100 * (x + y)
    se debe convertir el array a una matriz x,y
    en cada 1 se debe renderizar un foco en la matriz
    el fitnes aumenta en 4 cada que encuentra un 0 en la matriz al ser una zona sin liminosidad
    """
    # print(x)
    fitnes = 0
    contenedor_muestra = contenedor_vacio
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
            

#example_list = [ 0 for x in range(xl * yl) ]
#example_list[42] = 1
#example_list[92] = 1


#fit = fitness(indiv = example_list,long_gen=xl,num_lamparas=1,contenedor_vacio=contenedor)
    
def optimizar_poblacion(poblacion,num_lamparas):
    """
    tomar la poblacion y eliminar algunos 1 que es logico no son optimos
    """
    for i in range(len(poblacion)):
        # print(f"sujeto inicial \n{poblacion[i]}")
        
        posiciones = []
        lamparas = 0
        long_sujeto = len(poblacion[i])
        for j in range(long_sujeto):
            if poblacion[i][j] == 1:
                posiciones.append(j)
                lamparas += 1
        dif_lamparas = lamparas - num_lamparas
        if dif_lamparas > 0:
            distancia_inicio = 0 + posiciones[0]
            distancia_fin = (long_sujeto-1) - posiciones[len(posiciones)-1] 
            posicion_cambio = 0
            if distancia_fin <= distancia_inicio:
                posicion_tmp = len(posiciones) -1 
                posicion_cambio = posiciones[posicion_tmp]
            else:
                posicion_cambio = posiciones[0]
        poblacion[i][posicion_cambio] = 0
        #print(f"sujeto final \n{poblacion[i]}")
            
                 
            
    
    
def de(fobj, bounds, mut=1, crossp=0.7, popsize=30, its=500):
    dimensions = len(bounds)
    # generar poblacion
    pop = np.random.randint(limite_inferior, limite_superior, (popsize, dimensions))
    optimizar_poblacion(poblacion=pop,num_lamparas=num_lamparas)
    #x = input("ya termine")
    min_b, max_b = np.asarray([(0,1)] * len(bounds)).T
    diff = np.fabs(min_b - max_b)
    pop_denorm = min_b + pop * diff
    fitness = np.asarray([fobj(ind, long_gen=yl, num_lamparas=num_lamparas, contenedor_vacio=contenedor) for ind in pop_denorm])
    best_idx = np.argmin(fitness)
    best = pop_denorm[best_idx]
    
    
    for i in range(its):
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            a, b, c = pop[np.random.choice(idxs, 3, replace = False)]
            mutant = np.clip(a + mut * (b - c), 0, 1)
            cross_points = np.random.rand(dimensions) < crossp
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dimensions)] = True
            trial = np.where(cross_points, mutant, pop[j])
            trial_denorm = min_b + trial * diff
            f = fobj(trial_denorm, long_gen=yl, num_lamparas=num_lamparas, contenedor_vacio=contenedor)
            if f < fitness[j]:
                fitness[j] = f
                pop[j] = trial
                if f < fitness[best_idx]:
                    best_idx = j
                    best = trial_denorm
        if i % 100 == 0:
            print("El MEjor De La GEneracion  :  ", end="")
            print(best)
            print(str(f"generacion : {i} dimension : {dimensions} performance : {fobj(best,long_gen=yl, num_lamparas=num_lamparas, contenedor_vacio=contenedor)}"))

        yield best, fitness[best_idx]
        
    
# la dimension debe ser xl * yl
arr_len = xl * yl
for d in [arr_len]:
    it = list(de(fitness, [(limite_inferior, limite_superior)] * d, its=400))
    x, f = zip(*it)
    
