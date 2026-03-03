import numpy as np
import matplotlib.pyplot as plt

from skimage import measure
from pathlib import Path

#! Funcion a graficar
def func_F(x,y,z):
  return -x**2/9+y**2/16-z**2/4


def main():
  #! parametros para grafico
  Guardar_grafico = True
  Fondo_transparente = True
  Mostrar_grafico = True
  Equal_axis = False
  Texto_latex = True

  # tamaaño de fuentes
  tam_fuentes = 14

  if Texto_latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": tam_fuentes,
    })

  # intervalos para x,y,z
  intervalo_x = [-9,9]
  intervalo_y = [-9,9]
  intervalo_z = [-9,9]

  # Numero de subdivisiones en los ejes x, y, z
  N=100

  # Nivel de la superficie de nivel
  F_Level = 1

  #! comienza el proceso de graficar
  # puntos en los intervalos para el grafico
  x_points = np.linspace(*intervalo_x,N)
  y_points = np.linspace(*intervalo_y,N)
  z_points = np.linspace(*intervalo_z,N)

  # mallas para el grafico
  x_mesh, y_mesh, z_mesh = np.meshgrid(x_points,y_points,z_points)

  # Funcion para la superficie de nivel F(x,y,z)=F_Level
  F_Eval = func_F(x_mesh, y_mesh, z_mesh)

  # delta para marching cubes
  delta=[np.diff(x_points)[0],np.diff(y_points)[0],np.diff(z_points)[0]]

  # Evaluacion de la superficie de nivel F(x,y,z)=0
  verts, faces, _, _ = measure.marching_cubes(F_Eval,level=F_Level, spacing=delta)

  # trasladar los vertices a los limites para que los ejes esten bien ubicados
  verts += [intervalo_x[0],intervalo_y[0],intervalo_z[0]]

  # Preparar grafico 3D
  _ = plt.figure()
  ax = plt.axes(projection='3d')

  # Grafico 3D
  ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='gnuplot')#, lw=0)

  # Configurar grafico
  ax.set_xlim(*intervalo_x)
  ax.set_ylim(*intervalo_y)
  ax.set_zlim(*intervalo_z)
  ax.set_xlabel('$x$')
  ax.set_ylabel('$y$')
  ax.set_zlabel('$z$')
  if Equal_axis:
    ax.set_aspect('equal')

  #! Guardar grafico
  if Guardar_grafico:
    # Verificar si la carpeta imagenes existe, si no, crearla
    carpeta = Path('./imagenes/')
    if not carpeta.exists():
      carpeta.mkdir()

    # Obtener el nombre del archivo actual sin la extension
    Nombre = Path(__file__).stem

    # Nombre del archivo
    archivo = f'{carpeta}/{Nombre}.png'

    # Guardar la figura
    plt.savefig(archivo, dpi=600, transparent=Fondo_transparente)

  #! Mostrar la figura
  if Mostrar_grafico:
    plt.show()

if __name__=='__main__':
  main()