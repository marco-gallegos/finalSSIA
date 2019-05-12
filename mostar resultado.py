# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# longitudes
xl = 10
yl = 10
zl = 10

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