import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

def func_f(x,y):
  return np.sqrt(x**2+y**2)

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

  # definir los intervalos para x, y y z
  intervalo_x=[-5,5]
  intervalo_y=[-5,5]
  intervalo_z=[0,5]

  # numero de subdivisiones
  N=1000

  # puntos de los intervalos para el grafico
  x_points = np.linspace(*intervalo_x,N)
  y_points = np.linspace(*intervalo_y,N)

  # Crear las mallas para el grafico 3D
  x_mesh,y_mesh=np.meshgrid(x_points, y_points)
  z_mesh=func_f(x_mesh,y_mesh)

  # Cortar los valores de z si estan fuera de intervalo_z
  z_mesh[z_mesh>intervalo_z[1]]=np.nan
  z_mesh[z_mesh<intervalo_z[0]]=np.nan

  # Crear la figura
  _ , ax = plt.subplots(subplot_kw={'projection':'3d'})

  # Cambiar el angulo de la vista
  # ax.view_init(30, 30)

  # Configurar la figura
  ax.set_aspect('equal')
  ax.set_zlim3d(*intervalo_z)
  ax.set_xlim(*intervalo_x)
  ax.set_ylim(*intervalo_y)
  ax.set_xlabel('$x$')
  ax.set_ylabel('$y$')
  surf = ax.plot_surface(x_mesh,y_mesh,z_mesh,cmap='gnuplot')#,vmin=np.min(z_mesh),vmax=np.max(z_mesh))
  # fig.colorbar(surf,shrink=0.5,aspect=10,orientation='vertical')

  # Verificar si la carpeta imagenes existe, si no, crearla
  carpeta = Path('./imagenes/')
  if not carpeta.exists():
    carpeta.mkdir()

  # Obtener el nombre del archivo actual sin la extension
  Nombre = Path(__file__).stem

  # Nombre del archivo
  archivo = f'{carpeta}/{Nombre}.png'

  # Guardar la figura
  plt.savefig(archivo, dpi=600, transparent=True)

  # Mostrar la figura
  plt.show()

if __name__=='__main__':
  main()