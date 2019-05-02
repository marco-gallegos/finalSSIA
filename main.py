# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

def plotBox(ax, limite_x = 10, limite_y = 10, limite_z = 10):
    x = [0, limite_x]
    y = [0, limite_y]
    z = [p for p in range(limite_z)]
    for x_n in x:
        for y_n in y:
            ax.scatter3D(x_n,y_n,z,c=z,cmap="coolwarm")
    
    z = [limite_z]
    for x_n in range(limite_x+1):
        for y_n in range(limite_y+1):
            ax.scatter3D([x_n],[y_n],z)

nombre = "plotting box"

x = [0]
y = [0]
z = [x for x in range(100)]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("Ancho")
ax.set_ylabel("Largo")
ax.set_zlabel("Alto")

plotBox(ax,10,10,10)
# ax.scatter3D(x,y,z)
plt.show()