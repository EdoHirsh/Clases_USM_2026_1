import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Definir la función de dos variables
def func_f(x, y):
  return x**2 + y**2

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

  #* intervalos del grafico
  intervalo_x_graf = (-0.25, 5.25)
  intervalo_y_graf = (-0.25, 5.25)

  #* intervalos del dominio
  intervalo_x = (0, 5)
  intervalo_y = (0, 5)

  #* largo de los intervalos
  largo_x = intervalo_x[1] - intervalo_x[0]
  largo_y = intervalo_y[1] - intervalo_y[0]

  #* numero de subdivisiones
  n1 = 5
  n2 = 25
  n3 = 125

  #! Crear la figura
  fig = plt.figure(figsize=(15, 5))
  
  # numero de subdivisiones grafico 1
  n = n1
  dx = largo_x / n
  dy = largo_y / n

  # Crear los puntos de la cuadrícula
  x = np.linspace(*intervalo_x, n+1)
  y = np.linspace(*intervalo_y, n+1)
  X, Y = np.meshgrid(x, y)

  # Calcular los valores de la función en los puntos de la cuadrícula
  Z = func_f(X, Y)

  #* Crear la imagen 1
  ax = fig.add_subplot(131, projection='3d')
  ax.set_xlim(intervalo_x_graf)
  ax.set_ylim(intervalo_y_graf)
  ax.set_zlim(0, np.max(Z))

  #* Graficar las barras de la suma de Riemann
  for i in range(n):
    for j in range(n):
      x_i = i * dx
      y_j = j * dy
      z0 = 0 # Altura base de la barra
      # dz = func_f(x_i + dx/2, y_j + dy/2) # Altura de la barra por punto medio
      dz = func_f(x_i + dx, y_j + dy) # Altura de la barra por punto final
      color_bars = plt.cm.gnuplot((dz-np.min(Z)) / (np.max(Z)-np.min(Z)))
      ax.bar3d(x_i, y_j, z0, dx, dy, dz, color=color_bars, alpha=1, shade=True)
  # Configurar etiquetas y título
  ax.set_xlabel('$x$')
  ax.set_ylabel('$y$')
  ax.set_zlabel('$z$')
  # ax.set_title(f'Suma de Riemann de una función de dos variables (n={n})')
  ax.set_title(f'$m=n={n}$')

  #* Crear la imagen 2
  ax2 = fig.add_subplot(132, projection='3d')
  ax2.set_xlim(intervalo_x_graf)
  ax2.set_ylim(intervalo_y_graf)
  ax2.set_zlim(0, np.max(Z))

  # numero de subdivisiones grafico 2
  n = n2
  dx = largo_x / n
  dy = largo_y / n

  # Crear los puntos de la cuadrícula
  x = np.linspace(*intervalo_x, n+1)
  y = np.linspace(*intervalo_y, n+1)
  X, Y = np.meshgrid(x, y)

  # Calcular los valores de la función en los puntos de la cuadrícula
  Z = func_f(X, Y)

  #* Graficar las barras de la suma de Riemann
  for i in range(n):
    for j in range(n):
      x_i = i * dx
      y_j = j * dy
      z0 = 0 # Altura base de la barra
      # dz = func_f(x_i + dx/2, y_j + dy/2) # Altura de la barra por punto medio
      dz = func_f(x_i + dx, y_j + dy) # Altura de la barra por punto final
      color_bars = plt.cm.gnuplot((dz-np.min(Z)) / (np.max(Z)-np.min(Z)))
      ax2.bar3d(x_i, y_j, z0, dx, dy, dz, color=color_bars, alpha=1, shade=True)
  # Configurar etiquetas y título
  ax2.set_xlabel('$x$')
  ax2.set_ylabel('$y$')
  ax2.set_zlabel('$z$')
  # ax.set_title(f'Suma de Riemann de una función de dos variables (n={n})')
  ax2.set_title(f'$m=n={n}$')

  #* Crear la imagen 3
  ax3 = fig.add_subplot(133, projection='3d')
  ax3.set_xlim(intervalo_x)
  ax3.set_ylim(intervalo_y)
  ax3.set_zlim(0, np.max(Z))

  # numero de subdivisiones grafico 3
  n = n3
  dx = largo_x / n
  dy = largo_y / n

  # Crear los puntos de la cuadrícula
  x = np.linspace(*intervalo_x, n+1)
  y = np.linspace(*intervalo_y, n+1)
  X, Y = np.meshgrid(x, y)

  # Calcular los valores de la función en los puntos de la cuadrícula
  Z = func_f(X, Y)

  #* Graficar las barras de la suma de Riemann
  for i in range(n):
    for j in range(n):
      x_i = i * dx
      y_j = j * dy
      z0 = 0 # Altura base de la barra
      # dz = func_f(x_i + dx/2, y_j + dy/2) # Altura de la barra por punto medio
      dz = func_f(x_i + dx, y_j + dy) # Altura de la barra por punto final
      color_bars = plt.cm.gnuplot((dz-np.min(Z)) / (np.max(Z)-np.min(Z)))
      ax3.bar3d(x_i, y_j, z0, dx, dy, dz, color=color_bars, alpha=1, shade=True)
  # Configurar etiquetas y título
  ax3.set_xlabel('$x$')
  ax3.set_ylabel('$y$')
  ax3.set_zlabel('$z$')
  # ax.set_title(f'Suma de Riemann de una función de dos variables (n={n})')
  ax3.set_title(f'$m=n={n}$')

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