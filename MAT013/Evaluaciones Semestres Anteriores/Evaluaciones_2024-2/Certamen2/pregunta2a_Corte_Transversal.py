import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def func(x):
  return 4-x**2

def main ():
  # limites del eje x
  a=-4
  b=4
  # limites del eje y
  c=-4
  d=4

  # Nro. de subdivisiones en el eje x
  N=1000

  # Crear la figura
  fig, ax = plt.subplots()
  ax.set_aspect('equal')
  ax.set_xlim(a,b)
  ax.set_ylim(c,d)

  x = np.linspace(a,b,N)
  ax.plot(x,func(x))

  # Guardar la imagen
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  archivo = f'{carpeta}/pregunta2a_Corte_Transversal.png'

  fig.savefig(archivo, dpi=600, transparent=True)

  # Mostrar la imagen
  plt.show()

if __name__ == "__main__":
  main()