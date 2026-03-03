import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

def func_f(x,y):
  return np.sin(np.sqrt(x**2+y**2))

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

  # Definir los intervalos para x, y
  intervalo_x = [-10, 10]
  intervalo_y = [-10, 10]

  # Numero de subdivisiones
  N=1000

  # puntos de los intervalos para generar las mallas
  x_points = np.linspace(*intervalo_x, N)
  y_points = np.linspace(*intervalo_y, N)

  # Crear las mallas para el grafico
  x_mesh,y_mesh=np.meshgrid(x_points, y_points)
  z_mesh=func_f(x_mesh,y_mesh)

  # Crear la figura
  plt.imshow(z_mesh, extent=[*intervalo_x,*intervalo_y], origin='lower',interpolation='bicubic', cmap='gnuplot')

  # Etiquetas de los ejes
  plt.xlabel('$x$')
  plt.ylabel('$y$')
  plt.xticks([-10, -5, 0, 5, 10])#, ['$-10$', '$-5$', '$0$', '$5$', '$10$'])
  plt.yticks([-10, -5, 0, 5, 10])

  # Verificar si la carpeta imagenes existe, si no, crearla
  carpeta=Path('./imagenes/')
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