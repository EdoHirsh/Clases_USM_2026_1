import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

#* Definir las funciones de campo vectorial
# X= -x/(x^2+y^2)
# Y= -y/(x^2+y^2)
# es un caso malo que justifica normalizar y usar colores
def X_func(x,y):
  return x**2+y**2

def Y_func(x,y):
  return x**2-y**2

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

  # intervalos para x e y
  intervalo_x = [-5,5]
  intervalo_y = [-5,5]

  # numero de vectores (NxN)
  N=20

  # tamaño de las separaciones
  p_x=(intervalo_x[1]-intervalo_x[0])/N
  p_y=(intervalo_y[1]-intervalo_y[0])/N

  # puntos de los intervalos para generar las mallas
  x_points = np.arange(*intervalo_x,p_x)
  y_points = np.arange(*intervalo_y,p_y)

  # crear mallas para las bases los vectores
  x_mesh,y_mesh = np.meshgrid(x_points,y_points)
  
  # mallas de coordenadas de los vectores
  x_vec = X_func(x_mesh,y_mesh)
  y_vec = Y_func(x_mesh,y_mesh)

  # graficar los vectores
  fig=plt.figure()
  plt.quiver(x_mesh, y_mesh, x_vec, y_vec, color='b')
  plt.axis([*intervalo_x,*intervalo_y])

  # Etiquetas de los ejes
  plt.xlabel('$x$')
  plt.ylabel('$y$')
  # plt.grid()

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