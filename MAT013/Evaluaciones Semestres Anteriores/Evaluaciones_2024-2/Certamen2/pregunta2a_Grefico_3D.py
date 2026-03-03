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
  limites_x = [-4, 4]
  # limites del eje y
  limites_y = [-4, 4]
  # limites del eje z
  limites_z = [-4, 4]

  # numero de subdivisiones en los ejes x e y
  N=1000

  # coordenadas de los puntos en los ejes x e y
  x = np.linspace(*limites_x, N)
  y = np.linspace(*limites_y, N)

  # grafico superficie 3D f(x,y)
  X, Y = np.meshgrid(x, y)
  Z = func(X, Y)

  # truncar los valores de Z
  Z[Z<limites_z[0]] = np.nan
  Z[Z>limites_z[1]] = np.nan

  fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
  # proporciones de los ejes
  # ax.set_box_aspect([2,1,1])
  ax.plot_surface(X, Y, Z, cmap='gnuplot', edgecolor='none')

  # Guardar la imagen
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  archivo = f'{carpeta}/Pregunta2a_Grefico_3D.png'

  fig.savefig(archivo, dpi=600, transparent=True)

  # Mostrar la imagen
  plt.show()

if __name__ == "__main__":
  main()