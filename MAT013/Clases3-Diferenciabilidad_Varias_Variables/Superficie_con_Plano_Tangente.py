import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path

#! funcion de dos variables para graficar
def func(x, y):
    return x**2 + y**2

#* derivadas parciales
def func_x(x, y):
    return 2*x

def func_y(x, y):
    return 2*y

def main():
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

  #* limites de los ejes
  limites_x = [0,5]
  limites_y = [0,5]

  #* numero de subdivisiones en los ejes x e y
  N=500

  #* coordenadas del punto
  x_0 = 1
  y_0 = 1
  Punto = [x_0,y_0]

  x = np.linspace(*limites_x, N)
  y = np.linspace(*limites_y, N)

  #! grafico superficie 3D f(x,y)
  X, Y = np.meshgrid(x, y)
  Z = func(X, Y)
  ax=plt.axes(projection='3d')
  ax.set_xlabel(f'$x$', fontsize=tam_fuentes)
  ax.set_ylabel(f'$y$', fontsize=tam_fuentes)
  ax.set_zlabel(f'$z$', fontsize=tam_fuentes)

  surf=ax.plot_surface(X, Y, Z, cmap='gnuplot', edgecolor='none')

  #* plano tangente
  Z_p = func(*Punto)+func_x(*Punto)*(X-x_0)+func_y(*Punto)*(Y-y_0)
  plano=ax.plot_surface(X, Y, Z_p, cmap='gnuplot',vmin=np.min(Z),vmax=np.max(Z) , edgecolor='none')
  # plt.colorbar(surf, shrink=0.5)

  #! guardar grafico
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

  #! Mostrar grafico
  if Mostrar_grafico:
    plt.show()

if __name__ == "__main__":
  main()