import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

import matplotlib.pyplot as plt

def x_func(u, v) -> float:
  return (2+np.cos(v))*np.cos(u)

def y_func(u, v) -> float:
  return (2+np.cos(v))*np.sin(u)

def z_func(u, v) -> float:
  return np.sin(v)

def main () -> None:
  #* Define the parameter ranges
  u_min: float = 0
  u_max: float = 2*np.pi
  v_min: float = 0
  v_max: float = 2*np.pi

  #* Number of points in each direction
  N=100

  #* Define the ranges for the plot
  x_min: float = -4
  x_max: float = 4
  y_min: float = -4
  y_max: float = 4
  z_min: float = -2
  z_max: float = 2

  #* Define the parameter ranges
  u = np.linspace(u_min,u_max,N)
  v = np.linspace(v_min,v_max,N)

  #* Create a meshgrid from the parameters
  U, V = np.meshgrid(u, v)

  #* Define the parametric equations for the surface
  x = x_func(U, V)
  y = y_func(U, V)
  z = z_func(U, V)

  #* Create a 3D plot
  fig = plt.figure()
  ax = plt.axes(projection='3d')

  #* Propiedades del grafico
  ax.set_box_aspect([1,1,0.5])
  ax.set_xlim(x_min,x_max)
  ax.set_ylim(y_min,y_max)
  ax.set_zlim(z_min,z_max)
  ax.set_zticks([-2,-1,0,1,2])

  #* Graficar la superficie
  ax.plot_surface(x, y, z, cmap='gnuplot')
  # fig.colorbar(ax.plot_surface(x, y, z, cmap='gnuplot'))

  #* agregar etiquetas
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z')
  # ax.set_title('Superficie parametrica')

  #* guardar la imagen
  carpeta=Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  archivo = f'{carpeta}/Toro_parametrico.png'

  fig.savefig(archivo, dpi=300, transparent=True)

  # Mostrar la grafica
  plt.show()

if __name__ == "__main__":
  main()
