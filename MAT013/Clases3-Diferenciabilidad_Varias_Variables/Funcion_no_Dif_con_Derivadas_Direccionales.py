import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

#! funcion de dos variables para graficar
def func(x, y,n=3):
  return np.sqrt(x**2+y**2)*np.sin(n*np.arctan2(y,x))/2

def main () -> None:
  #! parametros para grafico
  Guardar_grafico = True
  Fondo_transparente = True
  Mostrar_grafico = True
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

  # limites del eje x
  x_min=-2
  x_max=2
  limites_x = [x_min,x_max]
  # limites del eje y
  y_min=-2
  y_max=2
  limites_y = [y_min,y_max]
  # limites del eje z
  z_min=-2
  z_max=2
  limites_z = [z_min,z_max]

  #densidad de puntos en los ejes x,y
  N=1000

  #periodo (n impar para derivadas direccionales consistentes en sentidos opuestos)
  n: int=3

  x = np.linspace(x_min,x_max,N)
  y = np.linspace(y_min,y_max,N)

  #* Preparar la grafico
  X, Y = np.meshgrid(x, y)
  Z = func(X, Y,n)

  #! Graficar la figura
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.set_xlim(*limites_x)
  ax.set_ylim(*limites_y)
  ax.set_zlim(*limites_z)
  ax.set_xlabel(f'$x$', fontsize=tam_fuentes)
  ax.set_ylabel(f'$y$', fontsize=tam_fuentes)
  ax.set_zlabel(f'$z$', fontsize=tam_fuentes)
  ax.set_aspect('equal')
  ax.set_xticks([-2,-1,0,1,2])
  ax.set_yticks([-2,-1,0,1,2])
  ax.set_zticks([-2,-1,0,1,2])

  ax.plot_surface(X, Y, Z,cmap='gnuplot', edgecolor='none')

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
    fig.savefig(archivo, dpi=600, transparent=Fondo_transparente)

  #! Mostrar grafico
  if Mostrar_grafico:
    plt.show()

if __name__ == "__main__":
  main()