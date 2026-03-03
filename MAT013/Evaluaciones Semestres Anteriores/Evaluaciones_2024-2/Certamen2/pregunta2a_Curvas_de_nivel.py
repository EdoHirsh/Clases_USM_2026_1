import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

#funcion de dos variables para graficar
def func(x, y):
  # return np.sqrt(y-2*x)
  # return y-2*x
  return 4-x**2-y**2

def main():
  # limites del eje x
  a=-4
  b=4
  # limites del eje y
  c=-4
  d=4

  # numero de subdivisiones en los ejes x e y
  N=1000

  # Niveles de las curvas de nivel
  Zlevels = [0,2]

  # coordenadas del dominio
  x = np.linspace(a, b, N)
  y = np.linspace(c, d, N)

  # Puntos superficie z=f(x,y)
  X, Y = np.meshgrid(x, y)
  Z = func(X, Y)

  fig,ax = plt.subplots()
  ax.set_aspect('equal')
  contours = ax.contour(X,Y,Z,cmap='gnuplot',vmin=np.min(Z),vmax=np.max(Z), levels=Zlevels)
  ax.clabel(contours,inline=1,fontsize=10)#,manual=[(0,1),(0,np.exp(1/2)),(0,np.exp(2))])

  # Guardar la imagen
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  archivo = f'{carpeta}/pregunta2a_Curvas_de_nivel.png'

  fig.savefig(archivo, dpi=600, transparent=True)

  # Mostrar la imagen
  plt.show()

if __name__=='__main__':
  main()