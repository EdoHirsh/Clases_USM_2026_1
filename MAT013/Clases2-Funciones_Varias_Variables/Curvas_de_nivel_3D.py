import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

def func_f(x,y,z):
  return np.sqrt(x**2+y**2)-z


def plot_Curvas3D(fn,ZLvls,N=100, bbox=(-2.5,2.5,-2.5,2.5,-2.5,2.5)):
  # establecer limites de los ejes
  xmin, xmax, ymin, ymax, zmin, zmax = bbox

  # iniciar la figura
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Puntos en los ejes
  A = np.linspace(xmin, xmax, N)
  B = np.linspace(ymin, ymax, N)

  # malla para graficar las curvas de nivel
  A1,A2 = np.meshgrid(A,B)

  # Graficar las curvas de nivel
  for z in ZLvls:
    X,Y = A1,A2
    Z = fn(X,Y,z)
    ax.contour(X, Y, Z+z, [z], zdir='z')

  # limites de los ejes
  ax.set_zlim3d(zmin,zmax)
  ax.set_xlim3d(xmin,xmax)
  ax.set_ylim3d(ymin,ymax)

  return fig

def main():
  # parametros de la figura
  Texto_latex = True

  # tamaaño de fuentes
  tam_fuentes = 14

  # configurar el texto en LaTeX
  if Texto_latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": tam_fuentes,
    })

  # Definir los intervalos para x, y y z
  intervalo_x = [-5,5]
  intervalo_y = [-5,5]
  intervalo_z = [0,5]

  # numero de subdivisiones
  N=1000

  # puntos para el grafico 3D
  x_points = np.linspace(*intervalo_x,N)
  y_points = np.linspace(*intervalo_y,N)

  # Crear las mallas para el grafico 3D
  x_mesh,y_mesh = np.meshgrid(x_points, y_points)
  z_mesh = func_f(x_mesh,y_mesh,0)

  # niveles de las curvas de nivel
  Zlevels=[1,2,3,4,5]
  # Zlevels=np.linspace(-5,5,20)

  # Crear la figura
  fig , ax = plt.subplots(subplot_kw={'projection':'3d'})

  # Configurar la figura
  ax.set_aspect('equal')
  ax.set_zlim3d(*intervalo_z)
  ax.set_xlim(*intervalo_x)
  ax.set_ylim(*intervalo_y)
  ax.set_xlabel('$x$')
  ax.set_ylabel('$y$')

  ax.contour(x_mesh, y_mesh, z_mesh, zdir='z', linewidths=1.5, cmap='gnuplot', levels=Zlevels)

  # Verificar si la carpeta imagenes existe, si no, crearla
  carpeta = Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  # Obtener el nombre del archivo actual sin la extension
  Nombre = Path(__file__).stem

  # Nombre del archivo
  archivo = f'{carpeta}/{Nombre}.png'

  # Guardar la figura
  fig.savefig(archivo, dpi=600, transparent=True)

  # Mostrar la figura
  plt.show()

if __name__=='__main__':
  main()