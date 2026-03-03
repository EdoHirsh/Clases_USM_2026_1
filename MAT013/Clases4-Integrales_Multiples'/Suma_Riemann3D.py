import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Definir la función de dos variables
def func_f(x, y):
  return x**2 + y**2

def main():
  #! parametros para grafico
  Guardar_grafico = False
  Fondo_transparente = False
  Mostrar_grafico = True
  Texto_latex = False

  # tamaaño de fuentes
  tam_fuentes = 14

  # configurar el texto en LaTeX
  if Texto_latex:
    plt.rcParams.update({
      "text.usetex": True,
      # "font.family": "Helvetica"
      "font.size": tam_fuentes,
    })

  #* intervalos del grafico
  intervalo_x_graf = (-0.25, 5.25)
  intervalo_y_graf = (-0.25, 5.25)

  #* intervalos del dominio
  intervalo_x = (0, 5)
  intervalo_y = (0, 5)

  #* largo de los intervalos
  largo_x = intervalo_x[1] - intervalo_x[0]
  largo_y = intervalo_y[1] - intervalo_y[0]

  # numero de subdivisiones
  n = 30
  dx = largo_x / n
  dy = largo_y / n

  # Crear los puntos de la cuadrícula
  x = np.linspace(*intervalo_x, n+1)
  y = np.linspace(*intervalo_y, n+1)
  X, Y = np.meshgrid(x, y)

  # Calcular los valores de la función en los puntos de la cuadrícula
  Z = func_f(X, Y)

  #! Crear la figura y el eje 3D
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Configurar la figura
  ax.set_xlim(intervalo_x_graf)
  ax.set_ylim(intervalo_y_graf)
  ax.set_xlabel('$x$')
  ax.set_ylabel('$y$')
  ax.set_zlabel('$z$')
  ax.set_title(f'Suma de Riemann de la función $f(x,y)=x^2+y^2$ ($m=n={n}$)')

  # # graficar la superficie con mayor detalle #!!(sin transparencia no se ve bien)
  # n_HD = 100
  # x_HD = np.linspace(*intervalo_x, n_HD)
  # y_HD = np.linspace(*intervalo_y, n_HD)
  # X_HD, Y_HD = np.meshgrid(x_HD, y_HD)
  # Z_HD = func_f(X_HD, Y_HD)
  # ax.plot_surface(X_HD, Y_HD, Z_HD, color='red', alpha=0.5)

  vol_aprox = 0  # Inicializar el área aproximada

  # Graficar las barras de la suma de Riemann
  for i in range(n):
    for j in range(n):
      x_i = i * dx
      y_j = j * dy
      z0 = 0 # Altura base de la barra
      dz = func_f(x_i + dx/2, y_j + dy/2) # Altura de la barra por punto medio
      # dz = func_f(x_i + dx, y_j + dy) # Altura de la barra por punto final
      # dz = func_f(x_i , y_j) # Altura de la barra por punto inicial
      # dz = (func_f(x_i + dx, y_j + dy)+func_f(x_i, y_j)) / 2  # Altura de la barra por promedio altura final e inicial
      color_bars = plt.cm.gnuplot((dz-np.min(Z)) / (np.max(Z)-np.min(Z)))
      ax.bar3d(x_i, y_j, z0, dx, dy, dz, color=color_bars, alpha=1, shade=True)
      vol_aprox += dz * dx * dy  # Sumar el volumen de cada barra a la área aproximada

  # mostrar el volumen aproximado
  plt.figtext(0.5, 0.01, f'Volumen aproximado: ${vol_aprox:.2f}$', ha='center', fontsize=12)

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

if __name__ == '__main__':
  main()