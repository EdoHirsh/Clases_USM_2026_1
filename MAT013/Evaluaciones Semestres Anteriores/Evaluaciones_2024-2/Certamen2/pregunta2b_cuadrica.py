import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

from pathlib import Path

def func(x,y,z):
  return 9*x**2 - (y**2) - 4*z**2 - 18*x - 8*z - 31
  # return ((x**2)*y+y**3)-z*x


def main():
  # Rango de valores para x,y,z
  limites_x = [-16,24]
  limites_y = [-4,4]
  limites_z = [-16,12]

  # Numero de subdivisiones en los ejes x, y, z
  N=50

  # Malla para el grafico 3D
  xl = np.linspace(*limites_x,N)
  yl = np.linspace(*limites_y,N)
  zl = np.linspace(*limites_z,N)
  X, Y, Z = np.meshgrid(xl,yl,zl)

  # Funcion para la superficie de nivel F(x,y,z)=0
  F = func(X, Y, Z)
  FLevel = 0

  # delta para marching cubes
  delta=[np.diff(xl)[0],np.diff(yl)[0],np.diff(zl)[0]]

  # Evaluacion de la superficie de nivel F(x,y,z)=0
  verts, faces, _, _ = measure.marching_cubes(F,level=FLevel, spacing=delta)

  # trasladar los vertices a los limites para que los ejes esten bien ubicados
  verts += [limites_x[0],limites_y[0],limites_z[0]]

  # Preparar grafico 3D
  fig = plt.figure()
  ax = plt.axes(projection='3d')

  # Grafico 3D
  ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='gnuplot')#, lw=0)
  # ax.set_aspect('equal')
  ax.set_xlim(*limites_x)
  ax.set_ylim(*limites_y)
  ax.set_zlim(*limites_z)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z')

  # guardar la imagen
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  archivo = f'{carpeta}/pregunta2b_cuadrica.png'

  fig.savefig(archivo, dpi=600, transparent=True)

  # Mostrar la imagen
  plt.show()

if __name__=='__main__':
  main()